import datetime
import redis

class FlightStatusTracker:
    ALLOWED_STATUSES = {'CANCELLED', 'DELAYED', 'ON TIME', 'ARRIVED'}


    def __init__(self, redis_instance=None):
        self.redis = redis_instance if redis_instance else redis.StrictRedis() 
 
        

    def change_status(self, flight, status):
        status = status.upper()
        if status not in self.ALLOWED_STATUSES:
            raise ValueError(
                "{} is not a valid status".format(status)
            )

        key = "flightno:{}".format(flight)
        value = "{}|{}".format(datetime.datetime.now().isoformat(), status)
        self.redis.set(key, value)
