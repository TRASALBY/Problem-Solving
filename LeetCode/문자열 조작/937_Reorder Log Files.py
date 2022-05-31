class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num_logs = []
        str_logs = []
        for log in logs:
            if log.split()[1].isdigit():
                num_logs.append(log)
            else:
                str_logs.append(log)
        str_logs.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        
        return(str_logs + num_logs)