def read_timer(story,wpm):
    if not isinstance(story, str):
        raise TypeError("Please input a string for `story`")
    
    if not isinstance(wpm, int):
        raise TypeError("Please input an integer for `wpm`")
    
    length_of_story = len(story.split())

    time_in_minutes = length_of_story/wpm

    minutes = int(time_in_minutes)

    seconds = int((time_in_minutes - minutes)* 60)
    
    return f'{minutes} minutes {seconds} seconds'