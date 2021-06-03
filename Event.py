import redis
from _datetime import datetime
from datetime import timedelta

class Campus_Festival:
    def __init__(self):
        redis_host = "localhost"
        redis_port = 6379
        self.r=redis.Redis(host=redis_host,
                           port=redis_port,
                           decode_responses=True)


    def venue(self, place):
        print("Venue : ")
            self.r.hset('venue', place)


    def create_new_event(start_time, venue, duration, name_of_person, phone_of_person):
        if self.r.sismember("phone_s_person", phone_of_person):
            print("person already exists")
        else:
            self.r.sadd("event_s_name", name_of_event)
            self.r.sadd("phone_s_person", phone_of_person)
            self.r.hmset("phone_h_person_" + phone_of_person,
            {
                "start_time":start_time,
                "venue":venue,
                "duration": duration,
                "name_of_event":name_of_event,
                "name_of_person":name_of_person,
                "phone_of_person": phone_of_person,
            }
            )
            print("Event created")

     def start_time(self):
        v_time=datetime.now().strftime("%Y%m%d%H%M%S")
        event_id = self.r.incr("event_id", 1)
        self.r.zadd("z_event", {v_time : event_id})

     def list_event(self):
        for i in self.r.smembers("phone_s_person"):
            print(i)

    def record_tickettype(self,name, birth_date, gender, ticket_type):
        self.r.sadd("event_s_guests", name)
        self.r.sadd("event_s_tickettypes", ticket_type)

        self.r.hmset("event_h_guest_" + name,
            {
                "name":name,
                "birth_date":birth_date,
                "gender":gender,
                "ticket_type":ticket_type

            })

    def list_of_guests(self):
        print("Guests:")
        for guest in self.r.smembers("event_h_guests"):
            print(guest)

    def list_ticket_types(self):
        print("Ticket Types:")
        for ticket in self.r.smembers("event_s_tickettypes"):
            print(ticket)

    def guest_likes_event(self, event_name):
        if self.r.sismember("event_s_name", event_name):
            if self.r.zscore("z_liked_events", event_name) == None:
                self.r.zadd("z_liked_events", event_name, 1)
            else:
                self.r.zincrby("z_liked_events", event_name, 1)
        else:
            print("Event not registered")

    def list_sorted_liked_events(self):
        print(self.r.zrange("z_liked_events",0, -1, withscores=True))

    def list_liked_events(self):
        print(self.r.zrange("z_liked_events", 0, -1))
