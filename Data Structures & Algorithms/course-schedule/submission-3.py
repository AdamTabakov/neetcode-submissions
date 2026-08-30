class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        path = set()
        graph = {}

        # to set up graph
        for course, prereq in prerequisites:
            if course not in graph:
                graph[course] = []
            graph[course].append(prereq)

        # dfs
        def dfs(course):
            # if the current course was already in the path, false due to a cycle
            if course in path:
                return False
            # if we have visited this course already, has to be true
            if course in visited:
                return True
            
            path.add(course)

            # for each prereq in the course 
            for prereq in graph.get(course, []):
                # if the return is false, return false
                if not dfs(prereq):
                    return False
            
            path.remove(course)
            visited.add(course)
            return True

        # for each course
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        
            