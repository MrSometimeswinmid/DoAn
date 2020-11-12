"""Class này triển khai những chức năng liên quan để việc xếp lịch.
Các chức năng phải được triển khai thành một class, và một phương thức emit() một signal.
Các xử lý logic của các chức năng được triển khai trong semester."""

from PyQt5.QtCore import pyqtSignal, QThread
from class_subject import Subject
from class_schedule import *
from class_conflict import *
from color import *




class Semester:
    """
    Class này là class trung gian giữa Subject và Table
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Class này chịu trách nhiệm hiển thị trực quan lịch của một Subject lên Table. Các thao tác liên quan đến Table
    có trên giao diện đều phải thông qua class này và các phương thức của nó.
    
    Trong Class này triển khai các xử lý logic và trả về cho giao diện.
    Nhiệm vụ của giao diện là bắt signal và cập nhật UI.
    """

    TIME_CHAINS = {
        '7:00:00':0,
        '9:00:00':1,
        '9:15:00':2,
        '10:15:00':3,
        '11:15:00':4,
        '13:00:00':5,
        '13:15:00':6,
        '14:00:00':7,
        '15:00:00':8,
        '15:15:00':9,
        '15:45:00':10,
        '16:15:00':11,
        '17:00:00':12,
        '17:15:00':13,
        '17:45:00':14,
        '18:45:00':15,
        '19:15:00':16,
        '21:00:00':17
        }

    DATE_CHAINS = {
        Monday: 0,
        Tuseday: 1,
        Wednesday: 2,
        Thursday: 3,
        Friday: 4,
        Saturday: 5,
        Sunday: 6,
        }
    
    # subject mà người dùng chọn sẽ nằm ở đây
    SUBJECTS = [] # CS414 1-8 CR 250 6-12  -> 12
    SEMESTERS = []
    # [
    #     [sub1, sub2, sub3, sub4], tuan 1
    #     [sub1, sub2, sub3, sub4], tuan 2
    #     [sub1, sub2, sub3, sub4],
    #     [sub1, sub2, sub3, sub4],
    #     [sub1, sub2, sub3, sub4],
    #     [sub1, sub2, sub3, sub4],
    #     [sub1, sub2, sub3, sub4],
    #     .....
    # ]
    SEMESTERS_INDEX = 0

    def getSubjectsInSemester(self) -> List[Subject]:
        return self.SUBJECTS
    
    def getTimeChains(self):
        return self.TIME_CHAINS

    def addSubjectToSemester(self, subject: Subject):
        self.SUBJECTS.append(subject)
        print(self.SUBJECTS)
        # self.initSemester()

    def deleteSubject(self, name):
        for j in range(len(self.SUBJECTS)):
            if self.SUBJECTS[j].getName() == name:
                self.SUBJECTS.pop(j)
                break

    def scanSubjectConflict(self) -> List[List[Dict[str,Tuple[str]]]]:
        """Bắt cặp tất cả Subject có trong danh sách trả về List chứa Conflicts.

        [[{'T6': ('9:15:00', '10:15:00')}, {'T6': ('7:00:00', '9:00:00')}, {'T6': ('7:00:00', '10:15:00')}]]"""
        conflicts = []
        output = []
        tempSubjectsList = self.SUBJECTS.copy()
        while len(tempSubjectsList) > 1:
            baseSubject = tempSubjectsList[0]
            for i in range(1,len(tempSubjectsList)):
                if i==len(tempSubjectsList):
                    break
                conflict = Conflit(baseSubject, tempSubjectsList[i])
                if conflict.isConflict():
                    conflicts.append(conflict)
            tempSubjectsList.pop(0)
        for conflict in conflicts:
            output.append(conflict.getConflitTime())
        return output

    def scanConflicts(self) -> List[Conflit]:
        conflicts = []
        tempSubjectsList = self.SUBJECTS.copy()
        while len(tempSubjectsList) > 1:
            baseSubject = tempSubjectsList[0]
            for i in range(1,len(tempSubjectsList)):
                if i==len(tempSubjectsList):
                    break
                conflict = Conflit(baseSubject, tempSubjectsList[i])
                if conflict.getConflitTime():
                    conflicts.append(conflict)
            tempSubjectsList.pop(0)
        return conflicts

    def getMaxWeekInSemester(self) -> int:
        """Trả về số Tuần kéo dài tối đa mà Semester có thể có."""
        max = 0
        for subject in self.SUBJECTS:
            print(self.SUBJECTS)
            if subject.getWeekRange()[1] > max:
                max = subject.getWeekRange()[1]
        return max

    def initSemester(self):
        """Mỗi Subject sẽ có số Tuần học cụ thể từ Tuần nào tới Tuần nào. Vì thế lấy số Tuần tối đa mà Subject có thể chiếm. 
        Sau đó thực hiện đổ từ Subject tương ứng vào các List. Mỗi List sẽ đại diện cho một Tuần học.
        """
        self.SEMESTERS = [[] for i in range(self.getMaxWeekInSemester())]
        print(self.SUBJECTS)
        for subject in self.SUBJECTS:
            for i in range(subject.getWeekRange()[0]-1, subject.getWeekRange()[1]):
                self.SEMESTERS[i].append(subject)
        return self.SEMESTERS

    def nextWeek(self):
        """Phương thức này sẽ tăng index của Semester lên 1. Thao tác trên biến SEMESTER_INDEX."""
        if self.SEMESTERS_INDEX < self.getMaxWeekInSemester():
            self.SEMESTERS_INDEX+=1
            self.SUBJECTS = self.SEMESTERS[self.SEMESTERS_INDEX]
            return 0
        else:
            return -1

    def previousWeek(self):
        """Phương thức này sẽ giảm index của Semester xuống 1. Thao tác trên biến SEMESTER_INDEX."""
        if self.SEMESTERS_INDEX > 0:
            self.SEMESTERS_INDEX-=1
            self.SUBJECTS = self.SEMESTERS[self.SEMESTERS_INDEX]
            return 0
        else:
            return -1