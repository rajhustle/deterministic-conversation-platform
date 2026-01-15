
import re
def guard(reply):
    if re.search(r'price|amount|cost|rs|\$', reply.lower()):
        return "A specialist can explain pricing. Would you like a callback?"
    if re.search(r'location|address|office', reply.lower()):
        return "Location details can be shared via a callback."
    return reply
