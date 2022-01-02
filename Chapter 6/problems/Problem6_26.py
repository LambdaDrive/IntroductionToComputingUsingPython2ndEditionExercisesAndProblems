def week():
    weekdays = {'Mo':'Monday', 'Tu':'Tuesday', 'We':'Wednesday', 'Th':'Thursday',
                'Fr':'Friday', 'Sa':'Saturday', 'Su':'Sunday'}
    while True:
        ab = input('Enter day abbreviation:')
        print(weekdays[ab])
