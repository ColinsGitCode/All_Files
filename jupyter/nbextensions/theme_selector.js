/*
 *  // Theme selector
 *  // Select your favorite code coloring
 */

define(["require"], function(require) {
    "use strict";

    var themes = {
        Default : "./themes/theme_default.css",
        arstotzka : "./themes/arstotzka.css",
        azure : "./themes/azure.css",
        bold : "./themes/bold.css",
        boxuk : "./themes/boxuk.css",
        carbonight : "./themes/carbonight.css",
        chocolate : "./themes/chocolate.css",
        crisp : "./themes/crisp.css",
        darkside : "./themes/darkside.css",
        earthsong : "./themes/earthsong.css",
        freshcut : "./themes/freshcut.css",
        frontier : "./themes/frontier.css",
        github : "./themes/github.css",
        gloom : "./themes/gloom.css",
        glowfish : "./themes/glowfish.css",
        goldfish : "./themes/goldfish.css",
        grunge : "./themes/grunge.css",
        halflife : "./themes/halflife.css",
        heroku : "./themes/heroku.css",
        hyrule : "./themes/hyrule.css",
        iceberg : "./themes/iceberg.css",
        juicy : "./themes/juicy.css",
        keen : "./themes/keen.css",
        kiwi : "./themes/kiwi.css",
        laravel : "./themes/laravel.css",
        lavender : "./themes/lavender.css",
        legacy : "./themes/legacy.css",
        mellow : "./themes/mellow.css",
        mintchoc : "./themes/mintchoc.css",
        mud : "./themes/mud.css",
        otakon : "./themes/otakon.css",
        pastel : "./themes/pastel.css",
        patriot : "./themes/patriot.css",
        peacock : "./themes/peacock.css",
        peacocks_in_space : "./themes/peacocks-in-space.css",
        peel : "./themes/peel.css",
        piggy : "./themes/piggy.css",
        potpourri : "./themes/potpourri.css",
        rainbow : "./themes/rainbow.css",
        revelation : "./themes/revelation.css",
        shrek : "./themes/shrek.css",
        slate : "./themes/slate.css",
        slime : "./themes/slime.css",
        snappy : "./themes/snappy.css",
        solarflare : "./themes/solarflare.css",
        sourlick : "./themes/sourlick.css",
        spearmint : "./themes/spearmint.css",
        stark : "./themes/stark.css",
        super : "./themes/super.css",
        tonic : "./themes/tonic.css",
        tribal : "./themes/tribal.css",
        tron : "./themes/tron.css",
        turnip : "./themes/turnip.css",
        yule : "./themes/yule.css",
        zacks : "./themes/zacks.css",
    };


    function add_to_toolbar(current_theme) {

        var ipython_toolbar = $(IPython.toolbar.element),
        	label = $('<span/>').addClass("navbar-text permissions-list").text('Theme:'),
        	select = $('<select/>').attr('id', 'permissions-select').attr('class', 'permissions-list form-control select-xs');

        // Add label to the toolbar
        ipython_toolbar.append(label).append(select);

        // Add themes to the selector
        for (var key in themes){
            select.append($('<option/>').attr('value', key).text(key));
        }

        // If actually a theme, select it
        if (current_theme){
            select.val(current_theme);
        }

        // Add an action when value is changed
        select.change( function(){
            theme_toggle($(this).val());
        });

    }

    function load_css(theme) {

        // Create a link element to attach the styles
        var link = document.createElement("link");
        link.type = "text/css";
        link.rel = "stylesheet";
        link.href = require.toUrl(themes[theme]);
        link.id = theme + "-css";
        document.getElementsByTagName("head")[0].appendChild(link);
    }

    function unload_css(theme) {

        // Select the theme to unload and remove the link node
        var css = document.getElementById(theme + "-css");
        css.parentNode.removeChild(css);
    }


    function theme_toggle(new_theme) {
    	
        var current_theme = window.localStorage.getItem('nb-theme');

        // Check if there is a theme actually loaded
        if (current_theme) {
            unload_css(current_theme);
        }

		load_css(new_theme);
        window.localStorage.setItem('nb-theme', new_theme);
    }

    function load_theme_selector() {
        
        var current_theme = window.localStorage.getItem('nb-theme');

        add_to_toolbar(current_theme);

        if (current_theme) {
            load_css(current_theme);
        }
                
    }

    return {
        load_ipython_extension: load_theme_selector
    };

});
