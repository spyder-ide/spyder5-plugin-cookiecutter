# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}
#
# Licensed under the terms of the {{ cookiecutter.open_source_license }}
# ----------------------------------------------------------------------------
"""
{{cookiecutter.project_name}} Main Widget.
"""

{% if cookiecutter.plugin_type == 'Spyder Dockable Plugin' %}
# Third party imports
from qtpy.QtWidgets import QHBoxLayout, QLabel
{% endif %}

# Spyder imports
from spyder.api.translations import get_translation
{% if cookiecutter.plugin_type == 'Spyder Dockable Plugin' %}
from spyder.api.widgets.main_widget import PluginMainWidget
{% else %}
from spyder.api.widgets.mixins import SpyderWidgetMixin
{% endif %}

# Localization
_ = get_translation("{{cookiecutter.project_package_name}}.spyder")


{% if cookiecutter.plugin_type == 'Spyder Dockable Plugin' -%}
class {{cookiecutter.project_name.replace(" ", "")}}Actions:
    ExampleAction = "example_action"


class {{cookiecutter.project_name.replace(" ", "")}}ToolBarSections:
    ExampleSection = "example_section"


class {{cookiecutter.project_name.replace(" ", "")}}OptionsMenuSections:
    ExampleSection = "example_section"


class {{cookiecutter.project_name.replace(" ", "")}}Widget(PluginMainWidget):

    # Signals

    def __init__(self, name=None, plugin=None, parent=None):
        super().__init__(name, plugin, parent)

        # Create an example label
        self._example_label = QLabel("Example Label")

        # Add example label to layout
        layout = QHBoxLayout()
        layout.addWidget(self._example_label)
        self.setLayout(layout)

    # --- PluginMainWidget API
    # ------------------------------------------------------------------------
    def get_title(self):
        return _("{{cookiecutter.project_name}}")

    def get_focus_widget(self):
        pass

    def setup(self, options=DEFAULT_OPTIONS):
        # Create an example action
        example_action = self.create_action(
            name={{cookiecutter.project_name.replace(" ", "")}}Actions.ExampleAction,
            text="Example action",
            tip="Example hover hint",
            icon=self.create_icon("spyder"),
            icon_text="Example icon text",
            triggered=lambda: print("Example action triggered!"),
        )

        # Add an example action to the plugin options menu
        menu = self.get_options_menu()
        self.add_item_to_menu(
            example_action,
            menu,
            {{cookiecutter.project_name.replace(" ", "")}}OptionsMenuSections.ExampleSection,
        )

        # Add an example action to the plugin toolbar
        toolbar = self.get_main_toolbar()
        self.add_item_to_toolbar(
            example_action,
            toolbar,
            {{cookiecutter.project_name.replace(" ", "")}}OptionsMenuSections.ExampleSection,
        )

    def update_actions(self):
        pass

    # --- Public API
    # ------------------------------------------------------------------------
{% endif -%}
