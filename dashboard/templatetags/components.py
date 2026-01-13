from django import template

register = template.Library()


def _percent_color(percent: str):
    """
    Terima string seperti '+12%', '-2%', '0%', dll.
    """
    if not percent:
        return None
    p = percent.strip()
    if p.startswith("-"):
        return "danger"   # merah
    if p.startswith("+"):
        return "success"  # hijau
    return "secondary"    # netral


@register.inclusion_tag("components/stat_card.html")
def stat_card(icon, label, value, percent=None, icon_bg="primary"):
    return {
        "icon": icon,
        "label": label,
        "value": value,
        "percent": percent,
        "percent_color": _percent_color(percent),
        "icon_bg": icon_bg
    }
