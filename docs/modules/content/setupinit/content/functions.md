Back to [All Modules](https://github.com/pyrustic/setupinit/blob/master/docs/modules/README.md#readme)

# Module Overview

**setupinit**
 
No description

> **Classes:** &nbsp; None
>
> **Functions:** &nbsp; [\_update\_manifest](#_update_manifest) &nbsp;&nbsp; [\_update\_setup\_cfg](#_update_setup_cfg) &nbsp;&nbsp; [get\_app\_pkg](#get_app_pkg) &nbsp;&nbsp; [get\_missing\_files](#get_missing_files) &nbsp;&nbsp; [get\_project\_name](#get_project_name) &nbsp;&nbsp; [get\_required\_filenames](#get_required_filenames) &nbsp;&nbsp; [initialize](#initialize) &nbsp;&nbsp; [initialized](#initialized)
>
> **Constants:** &nbsp; None

# All Functions
[\_update\_manifest](#_update_manifest) &nbsp;&nbsp; [\_update\_setup\_cfg](#_update_setup_cfg) &nbsp;&nbsp; [get\_app\_pkg](#get_app_pkg) &nbsp;&nbsp; [get\_missing\_files](#get_missing_files) &nbsp;&nbsp; [get\_project\_name](#get_project_name) &nbsp;&nbsp; [get\_required\_filenames](#get_required_filenames) &nbsp;&nbsp; [initialize](#initialize) &nbsp;&nbsp; [initialized](#initialized)

## \_update\_manifest
None



**Signature:** (data, project\_dir)





**Return Value:** None.

[Back to Top](#module-overview)


## \_update\_setup\_cfg
None



**Signature:** (data, project\_dir)





**Return Value:** None.

[Back to Top](#module-overview)


## get\_app\_pkg
This function extracts the application package name from a project_dir.
Basically it extracts the basename from the path then turns dashes "-" into
"underscores" "_".




**Signature:** (project\_dir=None)

|Parameter|Description|
|---|---|
|project\_dir|str, path to the target project |





**Return Value:** ['str, the application package name.']

[Back to Top](#module-overview)


## get\_missing\_files
Returns a dict of missing required files in a project




**Signature:** (project\_dir=None)

|Parameter|Description|
|---|---|
|project\_dir|str, the path to the project root. By default, os.getcwd is called |





**Return Value:** ['Returns a dict of missing filenames.', 'The keys of the dict are the canonical names of the missing files.', "The values are missing filenames (obviously these filenames doesn't exist).", 'Example: {"setup_cfg": "/path/to/filename/that/should/exist", ...}']

[Back to Top](#module-overview)


## get\_project\_name
This function returns the project name.
Basically it extracts the basename from the path




**Signature:** (project\_dir=None)

|Parameter|Description|
|---|---|
|project\_dir|str, path to the target project |





**Return Value:** ['str, the project name.']

[Back to Top](#module-overview)


## get\_required\_filenames
Returns a dict of required filenames.




**Signature:** (project\_dir=None)

|Parameter|Description|
|---|---|
|project\_dir|str, the path to the project root. By default, os.getcwd is called |





**Return Value:** ['Returns a dict.', 'The keys of the dict are the canonical names of the required files.', 'The values are filenames as they should be if these files exist.', 'Example: {"setup_cfg": "/path/to/filename/that/should/exist", ...}']

[Back to Top](#module-overview)


## initialize
Initialize a project by populating it with required files and directories.
These files are pre-filled with useful data.




**Signature:** (project\_dir=None)

|Parameter|Description|
|---|---|
|project\_dir|str, the path to the project root. By default, os.getcwd is called|





**Return Value:** None.

[Back to Top](#module-overview)


## initialized
Check if a Python project is initialized.
This function checks the files present in the root against a list of
required filenames (see the function: get_required_filenames())




**Signature:** (project\_dir=None)

|Parameter|Description|
|---|---|
|project\_dir|str, the path to the project root. If you don't set a path, the value of 'os.getcwd()' will be used |





**Return Value:** ['Returns True if the project is initialized, else returns False']

[Back to Top](#module-overview)


