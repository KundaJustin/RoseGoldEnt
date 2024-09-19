from django import template
from home.models import GalleryDetailsPage

register = template.Library()


@register.simple_tag
def latest_galleries(count=3):
    pages = GalleryDetailsPage.objects.live().order_by("-first_published_at")[:count]

    galleries_with_first_image = []
    for page in pages:
        first_gallery = (
            page.gallery_details.first()
        )  

        print(first_gallery.picture.images)
        if first_gallery:
            galleries_with_first_image.append((page, first_gallery))

    return galleries_with_first_image
