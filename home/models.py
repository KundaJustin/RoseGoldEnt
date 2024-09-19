from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from modelcluster.models import ClusterableModel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render

from home.blocks import FeaturedSectionBlock, GallerySectionBlock, HeroBlock, TeamBlock


class HomePage(Page):
    body = StreamField(
        [
            ("hero_section", HeroBlock()),
            ("gallery_section", GallerySectionBlock()),
            ("team_section", TeamBlock()),
            ("featured_gallery", FeaturedSectionBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class Category(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            suffix = 1

            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{suffix}"
                suffix += 1

        super().save(*args, **kwargs)


class Gallery(models.Model):
    images = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    title = models.CharField(max_length=1000, db_index=True)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="category", null=True
    )

    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")
        ordering = ["-date"]

    @property
    def image(self):
        try:
            return self.images.get_rendition("fill-50x50").img_tag()
        except:
            return ""

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            suffix = 1

            while Gallery.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{suffix}"
                suffix += 1

        super().save(*args, **kwargs)


class GalleryPage(models.Model):
    page = ParentalKey(
        "GalleryPages", on_delete=models.CASCADE, related_name="galleries"
    )
    gallery = models.ForeignKey(
        Gallery, on_delete=models.CASCADE, related_name="gallery_page"
    )

    panels = [FieldPanel("gallery"), FieldPanel("page")]

    def __str__(self):
        return str(self.gallery)


class GalleryPages(Page, ClusterableModel):
    content_panels = Page.content_panels + [
        InlinePanel("galleries", label="Gallery"),
    ]

    parent_page_types = ["HomePage"]
    subpage_types = []

    def get_context(self, request):
        context = super().get_context(request)
        context["galleries"] = self.galleries.select_related("gallery").all()
        return context


class GalleriesDetailPage(models.Model):
    page = ParentalKey(
        "GalleryDetailsPage", on_delete=models.CASCADE, related_name="gallery_details"
    )
    picture = models.ForeignKey(
        "Gallery", on_delete=models.CASCADE, related_name="gallery_details_page"
    )

    panels = [
        FieldPanel("picture"),
    ]

    def __str__(self):
        return str(self.picture)


class GalleryDetailsPage(RoutablePageMixin, Page):
    content_panels = Page.content_panels + [
        InlinePanel("gallery_details", label="Pictures"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["galleries"] = self.gallery_details.select_related("picture").all()
        return context

    @route(r"^gallery/(?P<slug>[-\w]+)/$", name="gallery_details_page")
    def gallery_detail_view(self, request, slug):
        return render(request)
