import logging
from typing import List, Any, Optional, Type, Dict, Tuple

import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine, and_, text, desc, or_
from sqlalchemy.orm import sessionmaker
from app.core.config_manager import ConfigManager
from app.core.db.db_model import Student, Teacher, Section, TeacherSection

logger = logging.getLogger(__name__)


class DBManager:

    def __init__(self, configManager: ConfigManager):
        self.dbType = configManager.getDBType()
        self.dbUrl = configManager.getDBUrl()
        self.engine = self._buildEngine()
        self.session = self.getSession()

    def _buildEngine(
        self,
    ):
        if self.dbType == "sqlite":
            # 'sqlite:///C:\\path\\to\\foo.db'
            return create_engine(f"sqlite:///{self.dbUrl}", echo=True)
        elif self.dbType == "mysql":
            # 'mysql+mysqldb://scott:tiger@localhost:3306/foo'
            return create_engine(f"mysql+mysqldb://{self.dbUrl}", echo=True)
        elif self.dbType == "postgresql":
            # 'postgresql+psycopg2://scott:tiger@localhost:5432/foo'
            return create_engine(f"postgresql+psycopg2://{self.dbUrl}", echo=True)
        else:
            raise NotImplementedError

    def getEngine(self):
        return self.engine

    def getSession(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    def insertRow(self, row):
        result = False
        session = self.getSession()
        try:
            session.add(row)
            session.commit()
            result = True
        except Exception as e:
            logger.warning(f"Unable to insert row with exception {e}")
        finally:
            session.close()
            return result

    def removeRow(self, row):
        """
        Remove a row in a table
        :param row:
        :return:
        """
        result = False
        session = self.getSession()
        try:
            session.delete(row)
            session.commit()
            result = True
        except Exception as e:
            logger.warning(f"Unable to remove row with exception {e}")
        finally:
            session.close()
            return result

    def executeRawSqlQuery(self, sqlQuery: str) -> DataFrame:
        """
        This function takes a raw sql text, then run it in a sqlalchemy engine. At last, it converts the result
        into a pandas dataframe
        :param sqlQuery:
        :return:
        """
        conn = self.engine.connect()
        query = conn.execute(text(sqlQuery))
        df = pd.DataFrame(query.fetchall())
        conn.close()
        return df

    def getRows(self, objName) -> Any:
        session = self.getSession()
        rows = session.query(objName).all()
        session.close()
        return rows

    def getAllStudents(self) -> Any:
        session = self.getSession()
        all_students = session.query(Student).all()
        session.close()
        return all_students

    def getAllTeachers(self) -> Any:
        session = self.getSession()
        all_students = session.query(Teacher).all()
        session.close()
        return all_students

    def createTeacher(self, name, subject) -> Any:
        session = self.getSession()
        session.add(Teacher(name=name, subject=subject))
        session.close()
