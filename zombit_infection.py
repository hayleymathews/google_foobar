from operator import itemgetter

def answer(meetings):
    meetings = sorted(meetings, key= itemgetter(1))
    attended_meetings = []
    for meeting in list(meetings):
        if meetings:
            meet = meetings.pop(0)
            attended_meetings.append(meet)
            meet_start, meet_end = meet
            for meeting in list(meetings):
                if meet_end > meeting[0]:
                    meetings.remove(meeting)
    return(len(attended_meetings))
