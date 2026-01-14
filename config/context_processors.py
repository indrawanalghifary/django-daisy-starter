# from .navigation import SIDEBAR_MENU
# from .settings import SIDEBAR_MENU

# def sidebar_menu(request):
#     return {"SIDEBAR_MENU": SIDEBAR_MENU}

from django.urls import reverse, NoReverseMatch
from .settings import SIDEBAR_MENU, APP_NAME
# from .services.badges import get_badge_counts
def app_name(request):
    return {"APP_NAME": APP_NAME}

def sidebar_menu(request):
    # badge_counts = get_badge_counts(request.user)
    badge_counts = {}

    menu = []
    for block in SIDEBAR_MENU:
        block_copy = {**block}
        items = []

        for item in block.get("items", []):
            item_copy = {**item}
            u = item.get("url", "")

            # resolve URL (django name vs external)
            if u.startswith("http://") or u.startswith("https://"):
                item_copy["item_url"] = u
                item_copy["is_external"] = True
            else:
                try:
                    item_copy["item_url"] = reverse(u)
                except NoReverseMatch:
                    item_copy["item_url"] = "#"
                item_copy["is_external"] = False

            # badge logic
            badge_key = item.get("badge")
            if badge_key and isinstance(badge_key, str):
                badge_value = badge_counts.get(badge_key, 0)
                item_copy["badge"] = badge_value if badge_value > 0 else None
            else:
                item_copy["badge"] = item.get("badge")

            items.append(item_copy)

        block_copy["items"] = items
        menu.append(block_copy)

    return {"SIDEBAR_MENU": menu}
