from Campus_Festival import Campus_Festival

rf=Campus_Festival()

# rf.venue('Kalvinter')

# rf.create_new_eventr('Kalvinter',  , 'John', 703953394)
# rf.create_new_event('Kalvinter',  , 'Smith', 703953398)
# rf.create_new_event('Kalvinter',  , 'Angie', 703953396)
#

rf.start_time()

rf.list_event()

# rf.record_tickettype('John','23rd January,1989' ,'Male',VIP  )
# rf.record_tickettype('Smith','3rd December, 1988' ,'Male',Premium  )
#rf.record_tickettype('Angie','4th February, 2001' ,'Female',Economy  )

rf.list_of_guests()
#
rf.list_ticket_types()
#
#rf.guest_likes_event('singing')
#rf.guest_likes_event('dancing')
#rf.guest_likes_event('sports')

rf.list_sorted_liked_events()
#
rf.list_liked_events()

rf.try_split()
