from app.core.db.db_model import Base, Student, Section, Teacher, TeacherSection
from app.core.db.db_manager import DBManager
from app.core.config_manager import ConfigManager
import pathlib


def createTables(engine):
    Base.metadata.create_all(engine)


def dropAllTables(engine):
    Base.metadata.drop_all(engine)


def populateSection(session):
    s1 = Section(name="class1", classroom_number="A035")
    session.add(s1)
    session.commit()
    session.close()


def populateStudents(session):
    s1 = Student(section_id=1, name="Ada Lovelace", age=21, year=4)
    session.add(s1)
    session.commit()
    session.close()


def populateTeachers(session):
    t1 = Teacher(name="professor Sorbus", subject="computing")
    session.add(t1)
    session.commit()
    session.close()


def main():

    configManager = ConfigManager()
    dbManager = DBManager(configManager)
    engine = dbManager.getEngine()

    dropAllTables(engine)
    createTables(engine)

    populateSection(dbManager.session)
    populateStudents(dbManager.session)
    populateTeachers(dbManager.session)


if __name__ == "__main__":
    main()
