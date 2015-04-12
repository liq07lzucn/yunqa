#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from atom.api import Subclass, Unicode

from enaml.widgets.api import Container
from enaml.workbench.api import PluginManifest
from workflow.api import Worknode


import enaml
with enaml.imports():
    from second_view import SecondView, SecondManifest

class SampleWorknode(Worknode):
    """ A custom Worknode class for the crash course example.

    This Worknode class will instantiate the content and register an
    additional plugin with the workbench when it is started. The extra
    plugin can be used to add addtional functionality to the workbench
    window while this Worknode is active. The plugin is unregistered
    when the Worknode is stopped.

    """
    #: The enamldef'd Container to create when the workbench is started.
    content_def = Subclass(Container)

    #: The enamldef'd PluginManifest to register on start.
    manifest_def = Subclass(PluginManifest)

    #: Storage for the plugin manifest's id.
    _manifest_id = Unicode()

    def start(self):
        """ Start the Worknode instance.

        This method will create the container content and register the
        provided plugin with the workbench.

        """
        self.content_def = SecondView    
        self.manifest_def = SecondManifest
        
        
        self.content = self.content_def()
        manifest = self.manifest_def()
        self._manifest_id = manifest.id
        self.workbench.register(manifest)

    def stop(self):
        """ Stop the Worknode instance.

        This method will unregister the Worknode's plugin that was
        registered on start.

        """
        self.workbench.unregister(self._manifest_id)
