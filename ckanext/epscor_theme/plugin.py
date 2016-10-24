import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Epscor_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'epscor_theme')


    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(Epscor_ThemePlugin, self).create_package_schema()
        #our custom field
        schema.update({
            'private-resource': [tk.get_validator('ignore_missing'),
				 tk.get_validator('boolean_validator'),
                                 tk.get_converter('convert_to_extras')]
        })
        return schema


    def update_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(Epscor_ThemePlugin, self).update_package_schema()
        #our custom field
        schema.update({
            'private-resource': [tk.get_validator('ignore_missing'),
				 tk.get_validator('boolean_validator'),
                                 tk.get_converter('convert_to_extras')]
        })
        return schema

    def show_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(Epscor_ThemePlugin, self).show_package_schema()
        #our custom field
        schema.update({
            'private-resource': [tk.get_validator('ignore_missig'),
                                 tk.get_converter('convert_from_extras')]
        })
        return schema
