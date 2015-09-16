#
# Copyright 2015 leenjewel
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os,sys
from ahandler import AHandler
try :
    import pyMySDKAPKBuilder.workspace
except ImportError :
    pwd = os.path.split(os.path.realpath(__file__))[0]
    sys.path.append(os.path.abspath(os.path.join(pwd, os.pardir, os.pardir)))
    import pyMySDKAPKBuilder.workspace

class BuildHandler(AHandler) :

    layout = "default.html"

    def get(self, workspace_name, project_id) :
        workspace_project = self.get_workspace(workspace_name, project_id)
        workspace_project.init_sdk()
        self.render("project.html", **{
            "is_create_project" : False,
            "is_build_project" : True,
            "workspace_name" : workspace_name,
            "project_name" : project_id,
            "workspace_project" : workspace_project,
            "workspace_sdks" : {sdk_config.get_config("id") : sdk_config for sdk_config in workspace_project.context["sdk_list"]},
        })

