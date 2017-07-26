cadcorp_version = '1.0'
cadcorp_vendor = 'West Yorkshire Police'

import gislink
import os.path

#Import logging modules
import logging

class DeveloperTools(gislink.Program):
    def   __init__(self):
        app_title = "Developer Tools"
        app_name=app_title.lower().replace(" ","_")
        super().__init__(name =   app_title)

        gislink_location=os.path.join(os.path.dirname(os.path.abspath(__file__)))
        icons_location=os.path.join(gislink_location,'icons')

        logging_config=os.path.join(gislink_location, "{}.logging".format(app_name))

        if os.path.isfile(logging_config):
            logging.config.fileConfig(logging_config)
        else:
            logging.basicConfig(level=logging.INFO)

        self.log=logging.getLogger(__name__)
        self.log.debug(__name__)

        try:
            self.application.ribbon_group.text=app_title
            
            # Create the Button Object and set a few attributes
            self.btn = gislink.RibbonButton(text="Toggle Program Window")
            self.btn.always_large_image = False
            self.btn.large_image = True

            self.btn.icon = os.path.join(icons_location, app_name + ".ico")

            # Add the click handler. The method has been defined below
            self.btn.click.add_handler(self.toggle_program_window)
            self.application.ribbon_group.add_control(self.btn)
        except Exception:
            self.log.exception('Unhandled Error initialising %s',app_title)

    def toggle_program_window(self, event):
        # API methods can be accessed from the event object in a click handler method.
        event.map_manager.DoCommand("AComShowProgramWindow")
