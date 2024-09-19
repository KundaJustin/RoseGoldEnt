from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
)
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/hero_block.html"


class GallerySectionBlock(StructBlock):
    page = blocks.PageChooserBlock(required=False, target_model="home.GalleryPages")

    class Meta:
        icon = "image"
        template = "blocks/gallery_section_block.html"

class PersonBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    name = CharBlock(required=False)
    title = CharBlock(required=False)
    description = CharBlock(required=False)


class TeamBlock(StructBlock):
    members = blocks.ListBlock(PersonBlock())

    class Meta:
        icon = "image"
        template = "blocks/team_block.html"


class FeaturedSectionBlock(StructBlock):
    page = blocks.PageChooserBlock(
        required=False, target_model="home.GalleryDetailsPage"
    )

    class Meta:
        icon = "image"
        template = "blocks/featured_gallery_section_block.html"
