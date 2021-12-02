from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from wagtail.core.models import Page
from wagtail.core import blocks, models
from wagtail.core.blocks.field_block import PageChooserBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock
# from wagtailstreamforms.blocks import WagtailFormBlock


class ChildDetails(blocks.StructBlock):
    """Child information"""

    
    child_details = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("identity_no", blocks.CharBlock(required = True, help_text = "This an autogenerated number")),
                ("district", blocks.CharBlock(required = True, help_text = "District")),
                ("health_center", blocks.CharBlock(required = True, help_text = "Where Child got Registered")),
                ("child_name", blocks.CharBlock(required = True, help_text = "Childe Name")),
                ("sex", blocks.CharBlock(required = True, help_text = "Sex")),
                ("dob", blocks.CharBlock(required = True, help_text = "Date of Birth")),
                ("birth_weight", blocks.CharBlock(required = True, help_text = "Weight of child in Kilograms")),
                ("birth_order", blocks.CharBlock(required = True, help_text = "Child Birth Order")),
                ("subcounty", blocks.CharBlock(required = True, help_text = "Sub-County")),
                ("parish", blocks.CharBlock(required = True, help_text = "Parish")),
                ("lc1", blocks.CharBlock(required = True, help_text = "Village")),
                ("special_care", blocks.CharBlock(required = True, help_text = "Tick reason for Special Care")),
                ("other_reasons", blocks.CharBlock(required = True, help_text = "Any other reason for special attention")),
                

            ]
        )

    )

    mother_details = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("mother_name", blocks.CharBlock(required = True, help_text = "Mother's Name")),
                ("mother_occupation", blocks.CharBlock(required = True, help_text = "Mother's Occupation")),
                ("nin", blocks.CharBlock(required = True, help_text = "National Identification Number")),
                ("father_name", blocks.CharBlock(required = True, help_text = "Father's Name")),
                ("father_occupation", blocks.CharBlock(required = True, help_text = "Father's Occupation")),
            ]
        )
    )

    class Meta:
        template = "streams/child_data.html"
        icon = "edit"
        label = "Child Data"