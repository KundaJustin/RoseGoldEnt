from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.admin.panels import FieldPanel, ObjectList, TabbedInterface
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.images.blocks import ImageChooserBlock

from home.models import Category, Gallery


class GallerySnippetViewSet(SnippetViewSet):
    model = Gallery
    menu_label = "Albums"
    menu_icon = "image"
    list_display = ["image", "title", "slug", "category", "date", UpdatedAtColumn()]
    edit_handler = TabbedInterface(
        [
            ObjectList(
                [
                    FieldPanel("title"),
                    FieldPanel("images"),
                    FieldPanel("category"),
                ],
                heading="Content",
            )
        ]
    )


class CategorySnippetViewSet(SnippetViewSet):
    model = Category
    menu_label = "Categories"
    menu_icon = "image"
    list_display = ["name", UpdatedAtColumn()]
    edit_handler = TabbedInterface(
        [
            ObjectList(
                [
                    FieldPanel("name"),
                ],
                heading="Content",
            )
        ]
    )


class GalleryMenuGroup(SnippetViewSetGroup):
    menu_label = "Gallery"
    menu_icon = "tag"
    menu_order = 200
    items = (GallerySnippetViewSet, CategorySnippetViewSet)


register_snippet(GalleryMenuGroup)
