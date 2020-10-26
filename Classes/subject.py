from typing import Tuple
from Classes.schedule import Schedule

class Subject:
    """
    # Subject đại diện cho một lớp học của một môn
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ## Các thông tin chính

    id: Mã lớp học.

    name: Tên lớp học.

    number_of_seats_left: Số chỗ còn lại.

    credits: Số tín chỉ.

    schedule: Một `Schedule` object đại diện cho thời gian của môn đó trong một Tuần học.

    teacher: Tên giảng viên.

    place: Nơi học.

    week_range: Tuần học.

    status: Tình trạng đăng ký.

    ## Subject, Semester và Table widget
    Class này sẽ giao tiếp với Semester để có thể vẽ màu trên Table widget.
    Các thuộc tính và phương thức của class này sẽ được team xây dựng đần trong các bản tới 😁😁

    http://courses.duytan.edu.vn/Sites/Home_ChuongTrinhDaoTao.aspx?p=home_coursesearch
    """

    def __init__(self, id: str, name: str, number_of_seats_left: int, credits: int, schedule: Schedule, teacher: str, place: str, week_range: list, status: int):
        self.id = id
        self.name = name
        self.number_of_seats_left = number_of_seats_left
        self.credits = credits
        self.schedule = schedule
        self.teacher = teacher
        self.place = place
        self.week_range = week_range
        self.status = status

    def getSchedule(self) -> Schedule:
        return self.schedule

    def getName(self) -> str:
        return self.name

    def __str__(self):
        return "<Subject {0}>".format(self.name)