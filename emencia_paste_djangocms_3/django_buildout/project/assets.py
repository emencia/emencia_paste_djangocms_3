"""
Available and enabled assets bundles for this project
"""
from django_assets import Bundle, register

AVALAIBLE_BUNDLES = {
    # Modernizr bundle, compatible for all Foundation releases
    'modernizr_js': Bundle(
        "js/foundation5/vendor/modernizr.js",
        filters='yui_js',
        output='js/modernizr.min.js'
    ),
    
    
    # Main CSS bundle For Foundation3
    'main_css': Bundle(
        'css/main.css',
        filters='yui_css',
        output='css/main.min.css'
    ),
    # Main Javascript bundle For Foundation3
    'main_js': Bundle(
        "js/foundation/jquery.js",
        #"js/foundation/jquery.foundation.forms.js",
        #"js/foundation/jquery.foundation.clearing.js",
        #"js/foundation/jquery.foundation.magellan.js",
        "js/foundation/jquery.foundation.orbit.js",
        #"js/foundation/jquery.foundation.navigation.js",
        #"js/foundation/jquery.foundation.accordion.js",
        "js/foundation/jquery.foundation.topbar.js",
        "js/foundation/jquery.cookie.js",
        #"js/foundation/jquery.foundation.joyride.js",
        #"js/foundation/jquery.foundation.tabs.js",
        "js/foundation/jquery.foundation.buttons.js",
        #"js/foundation/jquery.foundation.reveal.js",
        "js/foundation/jquery.event.swipe.js",
        #"js/foundation/jquery.foundation.alerts.js",
        "js/foundation/jquery.placeholder.js",
        #"js/foundation/jquery.foundation.tooltips.js",
        #"js/foundation/jquery.foundation.mediaQueryToggle.js",
        "js/foundation/jquery.event.move.js",
        "js/jquery/equalize.js",
        "js/jquery/addons.js",
        "js/foundation/app.js",
        filters='yui_js',
        output='js/main.min.js'
    ),
    
    
    # Main CSS bundle For Foundation5
    'app_css': Bundle(
        'css/flags.css',
        'css/app.css',
        filters='yui_css',
        output='css/app.min.css'
    ),
    # Main Javascript bundle For Foundation5
    'app_js': Bundle(
        "js/foundation5/vendor/jquery.js",
        #"js/foundation5/vendor/fastclick.js",
        #"js/foundation5/vendor/lodash.js", # This one is most used for Foundation development
        #"js/foundation5/vendor/jquery.placeholder.js", # This one is most used for Foundation development
        "js/foundation5/vendor/jquery.cookie.js",
        "js/foundation5/foundation/foundation.js",
        "js/foundation5/foundation/foundation.abide.js",
        "js/foundation5/foundation/foundation.accordion.js",
        "js/foundation5/foundation/foundation.alert.js",
        "js/foundation5/foundation/foundation.clearing.js",
        "js/foundation5/foundation/foundation.dropdown.js",
        #"js/foundation5/foundation/foundation.equalizer.js", # Foundation equalizer actually lacks of a responsive option like our addon
        "js/foundation5/foundation/foundation.interchange.js",
        "js/foundation5/foundation/foundation.joyride.js",
        "js/foundation5/foundation/foundation.magellan.js",
        "js/foundation5/foundation/foundation.offcanvas.js",
        "js/foundation5/foundation/foundation.reveal.js",
        "js/foundation5/foundation/foundation.slider.js",
        "js/foundation5/foundation/foundation.tab.js",
        "js/foundation5/foundation/foundation.tooltip.js",
        "js/foundation5/foundation/foundation.topbar.js",
        
        # For Orbit Slider (default used)
        "js/foundation5/foundation/foundation.orbit.js",
        
        ## For Royal Slider instead of Orbit (remember to enable its component in your 'app.scss')
        #"js/royalslider/dev/jquery.royalslider.js",
        #"js/royalslider/dev/modules/jquery.rs.video.js",
        #"js/royalslider/dev/modules/jquery.rs.thumbnails.js",
        #"js/royalslider/dev/modules/jquery.rs.auto-height.js",
        #"js/royalslider/dev/modules/jquery.rs.deeplinking.js",
        #"js/royalslider/dev/modules/jquery.rs.fullscreen.js",
        #"js/royalslider/dev/modules/jquery.rs.animated-blocks.js",
        #"js/royalslider/dev/modules/jquery.rs.autoplay.js",
        #"js/royalslider/dev/modules/jquery.rs.global-caption.js",
        #"js/royalslider/dev/modules/jquery.rs.visible-nearby.js",
        #"js/royalslider/dev/modules/jquery.rs.tabs.js",
        #"js/royalslider/dev/modules/jquery.rs.nav-auto-hide.js",
        #"js/royalslider/dev/modules/jquery.rs.autoplay.js",
        #"js/royalslider/dev/modules/jquery.rs.bullets.js",
        #"js/royalslider/dev/modules/jquery.rs.active-class.js",
        
        ## moment.js
        #"js/moment.js",
        
        # Magnific popup (modal window/pop-in)
        "js/jquery/magnific-popup.js",
        
        ## Masonry and socialaggregator libraries
        #"js/masonry/masonry.pkgd.js",
        #"js/socialaggregator.js",
        
        # Width/eight DOM element equalizer
        "js/jquery/equalize.js",
        
        ## Pikaday+moment.js for a datepicker
        #"js/pikaday.js",
        #"js/jquery/pikaday.jquery.js",
        
        "js/jquery/addons.js",
        "js/app.js",
        filters='yui_js',
        output='js/app.min.js'
    ),
}
ENABLED_BUNDLES = [
    'modernizr_js',
    'main_css',
    'main_js',
    'app_css',
    'app_js',
]

for item in ENABLED_BUNDLES:
    register(item, AVALAIBLE_BUNDLES[item])
