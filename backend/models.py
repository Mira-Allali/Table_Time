from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import enum

# ---------------------------------------------------------
# ENUM: TaskStatus
# ---------------------------------------------------------
# This defines possible values for the task status.
# Enum ensures that only predefined values can be used.
# It improves data consistency and avoids invalid inputs.
class TaskStatus(str, enum.Enum):
    PENDING = "pending"
    DONE = "done"


# ---------------------------------------------------------
# CLASS: Task (Database Table)
# ---------------------------------------------------------
# This class represents a table in the database.
# Each attribute corresponds to a column in the table.
class Task(Base):

    # Name of the table in the database
    __tablename__ = "tasks"

    # -----------------------------------------------------
    # COLUMN: id
    # -----------------------------------------------------
    # Primary key → unique identifier for each task
    # index=True → improves search performance
    id = Column(Integer, primary_key=True, index=True)

    # -----------------------------------------------------
    # COLUMN: title
    # -----------------------------------------------------
    # String column for task title
    # index=True → faster queries when filtering/searching
    title = Column(String, index=True)

    # -----------------------------------------------------
    # COLUMN: description
    # -----------------------------------------------------
    # Optional text field (nullable=True means it can be empty)
    description = Column(String, nullable=True)

    # -----------------------------------------------------
    # COLUMN: deadline
    # -----------------------------------------------------
    # Stores date and time of the task deadline
    deadline = Column(DateTime)

    # -----------------------------------------------------
    # COLUMN: status
    # -----------------------------------------------------
    # Stores task status as a string ("pending" or "done")
    # Default value is "pending"
    status = Column(String, default=TaskStatus.PENDING.value)