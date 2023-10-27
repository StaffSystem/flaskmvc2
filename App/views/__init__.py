# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .staff import staff_view
from .index import index_views
from .auth import auth_views
from .reviewList import reviewList_view

views = [user_views, index_views, auth_views,staff_view, reviewList_view] #something is staff view not working
# blueprints must be added to this list