class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        '''while len(students) > 0 and len(sandwiches) > 0:     
            if students[0] == sandwiches[0]:
                students=students[1:]
                sandwiches = sandwiches[1:]
            else:
                temp = students[0]
                students=students[1:]
                students.append(temp)
            if len(students) > 0 and len(sandwiches) > 0:
                if not any(x in students for x in sandwiches):
                    break
        return len(students)'''
        #if len(sandwiches)==0:
        #    return len(students)
        while sandwiches[0] in students:
            if students[0] == sandwiches[0]:
                students=students[1:]
                sandwiches = sandwiches[1:]
                if len(sandwiches) == 0:
                    return len(students)
            else:
                temp = students[0]
                students=students[1:]
                students.append(temp)
        return len(students)

