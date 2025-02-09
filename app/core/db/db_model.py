from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    section_id = Column("Section_id", Integer, ForeignKey("section.id"), nullable=False)
    name = Column("Name", String(255), nullable=False)
    age = Column("Age", Integer, nullable=True)
    year = Column("Year", Integer, nullable=False)
    section = relationship("Section")


class Section(Base):
    __tablename__ = "section"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String(255), nullable=False)
    classroom_number = Column("classroom_number", String(255), nullable=False)


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String(255), nullable=False)
    subject = Column("Subject", String(255), nullable=False)


class TeacherSection(Base):
    __tablename__ = "teacherClass"
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.id"), primary_key=True)
    section_id: Mapped[int] = mapped_column(ForeignKey("section.id"), primary_key=True)
    hour = Column("Hour", String(255), nullable=False)
    teacher: Mapped["Teacher"] = relationship("Teacher")
    section: Mapped["Section"] = relationship("Section")
