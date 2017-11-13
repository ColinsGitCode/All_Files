if (Jupyter) {
  $(Jupyter.events).on("app_initialized.NotebookApp", function() {

        var utils = require("base/js/utils");
        utils.load_extensions('theme_selector');
      
  });

} else {
  $([IPython.events]).on("app_initialized.NotebookApp", function() {
        IPython.load_extensions('theme_selector');
      
  });

}
