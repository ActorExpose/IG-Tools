import requests
from colorama import Fore
import sys  
import time 
import json
def wpplug():
    

    pl = ("""wordpress-importer
regenerate-thumbnails
wp-super-cache
jetpack
wordfence
wordpress-seo
tinymce-advanced
akismet
google-sitemap-generator
google-analytics-for-wordpress
contact-form-7
duplicate-post
wp-pagenavi
advanced-custom-fields
hello-dolly
nextgen-gallery
woocommerce
all-in-one-seo-pack
w3-total-cache
really-simple-captcha
siteorigin-panels
disable-comments
wp-multibyte-patch
google-analytics-dashboard-for-wp
black-studio-tinymce-widget
updraftplus
better-wp-security
wpclef
duplicator
ml-slider
googleanalytics
so-widgets-bundle
shortcodes-ultimate
redirection
ninja-forms
mailchimp-for-wp
breadcrumb-navxt
wp-mail-smtp
wp-optimize
wp-db-backup
backwpup
image-widget
broken-link-checker
si-contact-form
wp-smushit
tablepress
contact-form-7-to-database-extension
the-events-calendar
google-analyticator
wp-maintenance-mode
iwp-client
all-in-one-wp-security-and-firewall
post-types-order
wptouch
formidable
user-role-editor
captcha
wysija-newsletters
ewww-image-optimizer
force-regenerate-thumbnails
bbpress
custom-post-type-ui
add-to-any
page-links-to
yet-another-related-posts-plugin
wp-google-maps
widget-logic
yith-woocommerce-wishlist
si-captcha-for-wordpress
simple-page-ordering
contact-form-plugin
simple-custom-css
easy-google-fonts
types
disqus-comment-system
wp-statistics
photo-gallery
quick-pagepost-redirect-plugin
easy-fancybox
maintenance
seo-ultimate
cookie-law-info
sucuri-scanner
backupwordpress
redux-framework
antispam-bee
wp-clone-by-wp-academy
seo-image
instagram-feed
responsive-lightbox
ps-auto-sitemap
display-widgets
wordpress-popular-posts
worker
woosidebars
newsletter
wp-postviews
login-lockdown
wp-user-avatar
coming-soon
bwp-google-xml-sitemaps
recent-tweets-widget
addthis
social-media-widget
custom-sidebars
velvet-blues-update-urls
admin-menu-editor
buddypress
simple-social-icons
loco-translate
pretty-link
enable-media-replace
custom-facebook-feed
genesis-simple-edits
sidekick
php-code-widget
simple-301-redirects
taxonomy-terms-order
wp-retina-2x
mainwp-child
social-networks-auto-poster-facebook-twitter-g
simple-share-buttons-adder
all-in-one-wp-migration
underconstruction
adminimize
widget-importer-exporter
google-publisher
cookie-notice
polylang
wp-google-fonts
wp-dbmanager
wp-polls
simple-tags
official-statcounter-plugin-for-wordpress
social-media-feather
mailchimp
meta-box
wp-spamshield
wp-migrate-db
wp-fastest-cache
anti-spam
ultimate-coming-soon-page
simple-lightbox
gotmls
autoptimize
shareaholic
wp-edit
loginizer
share-this
youtube-embed-plus
slideshow-jquery-image-gallery
mappress-google-maps-for-wordpress
ultimate-tinymce
wp-slimstat
insert-headers-and-footers
intuitive-custom-post-order
search-and-replace
wordpress-23-related-posts-plugin
wp-lightbox-2
imsanity
options-framework
recent-posts-widget-extended
auto-post-thumbnail
contact-form-7-honeypot
members
title-remover
theme-my-login
p3-profiler
easy-theme-and-plugin-upgrades
add-meta-tags
sumome
slider-image
comprehensive-google-map-plugin
spacer
sg-cachepress
mce-table-buttons
amoforms
wp-social-bookmarking-light
all-in-one-event-calendar
iframe
wordpress-ping-optimizer
wp-sitemap-page
google-sitemap-plugin
wp-security-scan
facebook-like-box-widget
pubsubhubbub
rename-wp-login
events-manager
video-thumbnails
wp-instagram-widget
bulletproof-security
antivirus
facebook-comments-plugin
insert-php
pirate-forms
wp-editor
column-shortcodes
visual-form-builder
white-label-cms
yith-woocommerce-ajax-search
easy-wp-smtp
better-search-replace
theme-check
fancybox-for-wordpress
virtue-toolkit
xml-sitemap-feed
wordpress-backup-to-dropbox
cloudflare
password-protected
yith-woocommerce-compare
list-category-posts
cornerstone
advanced-code-editor
wp-jquery-lightbox
seo-automatic-links
revision-control
addquicktag
qtranslate-x
use-any-font
google-maps-widget
relevanssi
wp-postratings
cyr3lat
favicon-by-realfavicongenerator
simple-custom-post-order
custom-field-template
subscribe2
easy-table
google-language-translator
use-google-libraries
wp-jalali
google-document-embedder
easy-facebook-likebox
genesis-simple-hooks
simple-social-buttons
blogger-importer
disable-google-fonts
contact-form-7-datepicker
responsive-add-ons
ckeditor-for-wordpress
post-duplicator
yith-woocommerce-zoom-magnifier
advanced-excerpt
soliloquy-lite
easing-slider
genesis-enews-extended
custom-login
ps-disable-auto-formatting
cms-tree-page-view
search-everything
flamingo
gallery-plugin
smart-youtube
meteor-slides
count-per-day
wp-tab-widget
contact-form-builder
reveal-ids-for-wp-admin-25
dynamic-widgets
wp-review
automatic-updater
simple-image-widget
download-manager
master-slider
wp-recaptcha
wp-to-twitter
spam-free-wordpress
category-posts
tweet-old-post
bwp-minify
pushpress
child-theme-configurator
oauth-twitter-feed-for-developers
responsive-menu
genesis-responsive-slider
cyclone-slider-2
lightbox-gallery
siteguard
postman-smtp
add-from-server
peters-login-redirect
secure-wordpress
q2w3-fixed-widget
wp-shortcode
auto-terms-of-service-and-privacy-policy
option-tree
yith-woocommerce-ajax-navigation
megamenu
ultimate-social-media-icons
custom-permalinks
beaver-builder-lite-version
get-the-image
all-404-redirect-to-homepage
table-of-contents-plus
wp-paginate
timthumb-vulnerability-scanner
one-click-child-theme
sitemap
xcloner-backup-and-restore
nav-menu-roles
uk-cookie-consent
form-maker
hide-title
contextual-related-posts
csv-importer
stops-core-theme-and-plugin-updates
google-calendar-events
jquery-colorbox
header-footer
display-posts-shortcode
404-to-start
login-customizer
widgets-on-pages
download-monitor
custom-contact-forms
feedwordpress
zopim-live-chat
gallery-images
enhanced-media-library
subscribe-to-comments
facebook-pagelike-widget
wp-video-lightbox
newstatpress
simple-image-sizes
better-delete-revision
wp-job-manager
wp-google-map-plugin
wp-members
maxbuttons
search-regex
widget-css-classes
foobox-image-lightbox
nextend-facebook-connect
menu-icons
wpremote
amr-shortcode-any-widget
widget-settings-importexport
easy-twitter-feed-widget
wp-piwik
enhanced-text-widget
bad-behavior
really-simple-csv-importer
block-bad-queries
testimonials-widget
wp-smtp
printfriendly
email-address-encoder
exploit-scanner
portfolio-post-type
widget-context
sidebar-login
smk-sidebar-generator
accesspress-social-icons
custom-post-type-permalinks
taxonomy-metadata
multiple-post-thumbnails
codepress-admin-columns
lazy-load
baidu-sitemap-generator
sexybookmarks
404-to-301
floating-social-media-icon
categories-images
lockdown-wp-admin
wpcat2tag-importer
asesor-cookies-para-la-ley-en-espana
wordpress-popup
404-redirection
twitter-widget-pro
disable-xml-rpc-pingback
tiny-compress-images
rvg-optimize-database
movabletype-importer
jquery-collapse-o-matic
head-cleaner
wp-clean-up
testimonials-by-woothemes
wassup
advanced-access-manager
user-switching
clean-and-simple-contact-form-by-meg-nicholas
adrotate
verify-google-webmaster-tools
no-category-base-wpml
email-subscribers
login-with-ajax
editorial-calendar
amp
google-analytics-dashboard
wp-e-commerce
eu-cookie-law
advanced-responsive-video-embedder
growmap-anti-spambot-plugin
cryout-theme-settings
post-expirator
nk-google-analytics
wp-construction-mode
instagram-slider-widget
easy-digital-downloads
hyper-cache
bulk-delete
envira-gallery-lite
easy-bootstrap-shortcodes
twitter
wp-database-backup
jquery-updater
edit-author-slug
youtube-channel-gallery
wp-responsive-menu
powerpress
wpfront-user-role-editor
wp-copyprotect
wp-hide-post
syntaxhighlighter
simple-page-sidebars
leaflet-maps-marker
contact-form-7-dynamic-text-extension
google-captcha
remove-query-strings-from-static-resources
clone-posts
wp-product-review
crayon-syntax-highlighter
genesis-simple-sidebars
wp-all-import
paid-memberships-pro
wordpress-simple-paypal-shopping-cart
page-list
disable-xml-rpc
wp-spamfree
dynamic-featured-image
uber-login-logo
woocommerce-pdf-invoices-packing-slips
popup-maker
wp-author-date-and-meta-remover
wp125
recent-posts-widget-with-thumbnails
portfolio-gallery
facebook-button-plugin
wp-customer-reviews
simple-sitemap
accesspress-social-share
rss-importer
duracelltomi-google-tag-manager
wp-photo-album-plus
wp-subscribe
hupso-share-buttons-for-twitter-facebook-google
social-media-builder
post-thumbnail-editor
adminer
contact-form-to-email
feedburner-plugin
foogallery
contact-form-maker
wordpress-social-login
easy-adsense-lite
raw-html
zencache
wps-hide-login
mailchimp-forms-by-mailmunch
slideshow-gallery
post-type-archive-links
related-posts
wp-gallery-custom-links
user-photo
like-box
no-comments
coming-soon-maintenance-mode-from-acurax
tubepress
pdf-embedder
easy-social-icons
woocommerce-multilingual
eps-301-redirects
cleantalk-spam-protect
wp-google-analytics
user-access-manager
accesspress-social-counter
font
really-simple-facebook-twitter-share-buttons
backup
facebook-conversion-pixel
dynamic-to-top
wp-total-hacks
profile-builder
scroll-back-to-top
yikes-inc-easy-mailchimp-extender
wp-add-custom-css
paypal-donations
resize-image-after-upload
ad-injection
flash-album-gallery
post-type-switcher
favicon-rotator
feed-them-social
slider-wd
wp-pagenavi-style
visitor-maps
flickr-rss
wysiwyg-widgets
wp-print
multi-plugin-installer
bruteprotect
coming-soon-page
so-css
woocommerce-delivery-notes
wp-mail-bank
search-meter
wp-filebase
lightbox
widget-shortcode
html-sitemap
all-in-one-schemaorg-rich-snippets
s2member
compact-wp-audio-player
bj-lazy-load
wp-content-copy-protector
alpine-photo-tile-for-instagram
pods
site-is-offline-plugin
capability-manager-enhanced
multi-device-switcher
remove-category-url
call-now-button
gzip-ninja-speed-compression
gtranslate
menu-image
wordpress-database-reset
bootstrap-3-shortcodes
wp-rss-aggregator
ssh-sftp-updater-support
my-calendar
wonderm00ns-simple-facebook-open-graph-tags
event-organiser
youtube-embed
wp-simple-firewall
woocommerce-customizer
wpmandrill
easy-testimonials
gallery-video
woocommerce-grid-list-toggle
calendar
formget-contact-form
content-views-query-and-display-post-page
baw-login-logout-menu
wufoo-shortcode
any-mobile-theme-switcher
wp-content-copy-protection
oa-social-login
twitter-facebook-google-plusone-share
php-text-widget
spider-event-calendar
top-10
wp-crontrol
json-api
features-by-woothemes
dropdown-menu-widget
simple-map
theme-junkie-custom-css
pixtypes
social-sharing-toolkit
pinterest-pin-it-button
advanced-wp-columns
mashsharer
weaver-ii-theme-extras
cmb2
wp-updates-notifier
ultimate-posts-widget
wp-security-audit-log
advanced-iframe
no-page-comment
newsletter-sign-up
ag-custom-admin
varnish-http-purge
wp-useronline
easy-smooth-scroll-links
theme-test-drive
video-embed-thumbnail-generator
gallery-bank
stop-spammer-registrations-plugin
awesome-weather
simple-history
baw-post-views-count
wpide
posts-in-page
styles
custom-post-widget
crazy-bone
php-code-for-posts
audit-trail
magee-shortcodes
related-posts-thumbnails
flexi-pages-widget
font-awesome-4-menus
acurax-social-media-widget
smart-slider-3
tabby-responsive-tabs
woocommerce-checkout-manager
delete-all-comments
page-scroll-to-id
woocommerce-menu-bar-cart
contact-widgets
templatesnext-toolkit
debug-bar
genesis-title-toggle
ditty-news-ticker
ozh-admin-drop-down-menu
wowslider
mw-wp-form
rotatingtweets
better-analytics
woocommerce-colors
ultimate-member
advanced-image-styles
ultimate-maintenance-mode
aqua-page-builder
fourteen-colors
bwp-recaptcha
booking
video-sidebar-widgets
dropbox-backup
wp-admin-ui-customize
disable-emojis
custom-field-suite
rocket-maintenance-mode
admin-menu-tree-page-view
lightweight-social-icons
nginx-helper
wc-shortcodes
content-aware-sidebars
all-in-one-webmaster
insert-html-snippet
kk-star-ratings
add-link-to-facebook
contact-bank
accesspress-twitter-feed
really-simple-ssl
only-tweet-like-share-and-google-1
rss-includes-pages
ultimate-social-media-plus
woocommerce-google-analytics-integration
pixcodes
wunderground
ultimate-form-builder-lite
facebook-auto-publish
ultimate-responsive-image-slider
social-count-plus
statify
new-google-plus-badge-widget
remove-google-fonts-references
easy-pie-maintenance-mode
wp-flexible-map
my-custom-css
commentluv
codepeople-post-map
responsive-select-menu
mp3-jplayer
safe-redirect-manager
ad-inserter
svg-vector-icon-plugin
advanced-random-posts-widget
flexible-posts-widget
transposh-translation-filter-for-wordpress
google-maps
wp-insert
italy-cookie-choices
subscribe-to-comments-reloaded
popups
nextcellent-gallery-nextgen-legacy
ultimate-category-excluder
dirtysuds-embed-pdf
heartbeat-control
easy-pricing-tables
bm-custom-login
woocommerce-all-in-one-seo-pack
easy-watermark
speed-booster-pack
aryo-activity-log
pc-robotstxt
clicky
kiwi-logo-carousel
gallery-by-supsystic
disable-feeds
related-posts-by-zemanta
tiled-gallery-carousel-without-jetpack
erident-custom-login-and-dashboard
one-click-close-comments
under-construction-wp
better-font-awesome
easy-pie-coming-soon
nofollow
login-security-solution
add-logo-to-admin
attachments
sendgrid-email-delivery-simplified
sem-external-links
fonts
ga-google-analytics
carousel-without-jetpack
media-library-assistant
kimili-flash-embed
smooth-slider
custom-meta-widget
rss-footer
facebook-members
acf-field-date-time-picker
floating-social-bar
vaultpress
iq-block-country
ssl-insecure-content-fixer
fruitful-shortcodes
genesis-favicon-uploader
jquery-pin-it-button-for-images
amazon-web-services
woocommerce-csvimport
show-hide-author
facebook-page-promoter-lightbox
customizer-export-import
extended-categories-widget
unyson
simple-follow-me-social-buttons-widget
simply-exclude
svg-support
tracking-code-manager
menu-social-icons
homepage-control
wp-sendgrid
wp-noexternallinks
wp-sticky
recent-facebook-posts
wp-super-cache-clear-cache-menu
saphali-woocommerce-lite
wordpress-mobile-pack
wp-twitter-feeds
manual-image-crop
youtube-widget-responsive
yuzo-related-post
image-watermark
wp-better-emails
simple-google-map
easy-coming-soon
easy-social-share-buttons
intergeo-maps
duplicate-page-and-post
wp-external-links
testimonial-rotator
simply-instagram
jquery-t-countdown-widget
wpgform
landing-pages
wp-share-buttons-analytics-by-getsocial
woocommerce-exporter
footer-putter
favicon-xt-manager
itro-popup
buddypress-media
comet-cache
wordpress-access-control
remove-dashboard-access-for-non-admins
gantry
super-socializer
bulk-page-creator
gwolle-gb
drafts-scheduler
open-external-links-in-a-new-window
meta-manager
facebook-by-weblizar
hide-admin-bar-from-non-admins
fv-top-level-cats
smart-slider-2
kebo-twitter-feed
yop-poll
persian-woocommerce
schema-creator
optinmonster
code-snippets
embedplus-for-wordpress
calculated-fields-form
contact-form-7-mailchimp-extension
quotes-collection
wp-performance-score-booster
wp-fail2ban
google
tawkto-live-chat
stealth-login-page
metronet-reorder-posts
admin-management-xtended
newpost-catch
showcase-visual-composer-addon
jquery-smooth-scroll
post-snippets
child-themify
global-content-blocks
bootstrap-for-contact-form-7
custom-menu-wizard
wpfront-scroll-top
caldera-forms
simple-full-screen-background-image
fv-wordpress-flowplayer
wp-pro-quiz
link-library
custom-favicon
wp-facebook-open-graph-protocol
wp-site-migrate
featured-video-plus
mail-subscribe-list
woocommerce-product-archive-customiser
ad-widget
woocommerce-pagseguro
orbisius-child-theme-creator
wordpress-reset
custom-share-buttons-with-floating-sidebar
woocommerce-jetpack
email-encoder-bundle
addon-so-widgets-bundle
logo-slider
google-universal-analytics
rest-api
wp-ban
strictly-autotags
contact-form-email
simple-twitter-tweets
ifeature-slider
restricted-site-access
image-slider-widget
user-submitted-posts
easy-modal
rus-to-lat-advanced
wp-live-chat-support
stats-counter
backup-with-restore
projects-by-woothemes
wp-htaccess-control
lj-maintenance-mode
advanced-post-slider
gregs-high-performance-seo
wp-sweep
qtranslate-slug
google-maps-easy
grand-media
widgetize-pages-light
visitors-traffic-real-time-statistics
what-the-file
taxonomy-images
cpt-bootstrap-carousel
amazon-s3-and-cloudfront
polldaddy
wp-seo-qtranslate-x
cachify
robo-gallery
shortpixel-image-optimiser
posts-to-posts
rich-text-tags
co-authors-plus
easy-video-player
soundcloud-is-gold
go-live-update-urls
squirrly-seo
ecwid-shopping-cart
shortcoder
wp-math-captcha
genesis-translations
hide-my-site
paypal-for-woocommerce
advanced-sidebar-menu
yith-maintenance-mode
duplicate-menu
wp-email-login
simple-facebook-plugin
admin-custom-login
cimy-user-extra-fields
contact-form-manager
wordpress-easy-paypal-payment-or-donation-accept-plugin
wp-backitup
yith-woocommerce-quick-view
brute-force-login-protection
super-simple-google-analytics
wp-limit-login-attempts
header-and-footer-scripts
wordpress-language
i-recommend-this
wc-gallery
business-directory-plugin
js-composer-qtranslate-x
customify
advanced-ads
woocommerce-sequential-order-numbers
zero-spam
website-monetization-by-magenet
sydney-toolbox
groups
pagerestrict
bootstrap-shortcodes
css-javascript-toolbox
easy-image-gallery
analytics-counter
admin-post-navigation
horizontal-scrolling-announcement
woocommerce-shortcodes
mailgun
wordpress-social-ring
embed-any-document
magic-fields-2
wangguard
disable-wordpress-updates
vanilla-pdf-embed
postie
email-before-download
juiz-social-post-sharer
simple-maintenance-mode
yandex-metrika
breadcrumb-trail
wp-job-manager-contact-listing
social-share-buttons-by-supsystic
wp-maintenance
trust-form
sqlite-integration
social-media-icons-widget
captcha-on-login
post-views-counter
typekit-fonts-for-wordpress
alo-easymail
udinra-all-image-sitemap
youtube-channel
gigpress
rating-widget
wp-media-library-categories
wp-nested-pages
simple-ads-manager
genesis-simple-share
gravity-forms-custom-post-types
faster-pagination
advanced-text-widget
wplegalpages
player
json-rest-api
google-authenticator
genesis-connect-woocommerce
pinterest-pin-it-button-on-image-hover-and-post
cms-commander-client
contact-form-7-add-confirm
store-locator-le
ajax-load-more
facebook-thumb-fixer
instagram-for-wordpress
easy-media-gallery
wordpress-move
click-to-tweet-by-todaymade
improved-include-page
woocommerce-xml-csv-product-import
wp-hide-dashboard
https-redirection
formbuilder
tumblr-importer
wordpress-post-tabs
wp-job-manager-locations
welcome-email-editor
columns
wp-mobile-detect
acf-qtranslate
rss-post-importer
crazyegg-heatmap-tracking
our-team-enhanced
social-locker
accordion-shortcodes
seamless-donations
media-file-renamer
thesis-openhook
email-newsletter
wp-stats
flickr-badges-widget
uji-countdown
check-email
wp-editor-widget
alexa-internet
basic-google-maps-placemarks
wp-social-likes
synved-shortcodes
xml-sitemaps
nav-menu-images
email-users
mobble
woocommerce-correios
starbox
wp-recaptcha-integration
google-maps-builder
wp-page-widget
wp-social-sharing
ricg-responsive-images
new-user-approve
rss-import
nospamnx
public-post-preview
shortcode-widget
popup-by-supsystic
webriti-smtp-mail
magic-action-box
multiple-content-blocks
genesis-layout-extras
animate-it
simple-wp-sitemap
aweber-web-form-widget
""").split("\n")

    print(Fore.GREEN+" [+] "+Fore.WHITE+"Please Enter WordPress URL\n")
    print(Fore.YELLOW+" [!] "+Fore.WHITE+"Please Do Not Include Http\n")

    try:
        
        url = input(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+"~"+Fore.RED+"@Root"+Fore.WHITE+"/"+"CMS Detection Woedperess"+"/"+"Plugins"+Fore.GREEN+"""]
 └──╼  """+Fore.WHITE+"$ ").lower()
        if url == "" or None:
            time.sleep(1)
            print(Fore.GREEN+" [+] "+Fore.WHITE+"Please Enter The URL")
            time.sleep(0.3)
            sys.exit()

        s = requests.get("http://"+url+"/wp-content/plugins/")

        if s.status_code == 404 or s.status_code == 500:
            print(Fore.YELLOW+" [!] "+Fore.WHITE+"Site NOT Wordpress")
            sys.exit()
        else:
            pass
        time.sleep(0.5)
        print(Fore.YELLOW+" [!] "+Fore.WHITE+"Scanning 1000 Best plugins ...\n")
        time.sleep(4)
        print(Fore.YELLOW+" [!] "+Fore.WHITE+"Loading 1000 Plugins...\n")
        time.sleep(3)
        print(Fore.BLUE+" [*] "+Fore.WHITE+" Please Wait\n")

    except:
        print("")
        sys.exit()
    for plus in pl:
        time.sleep(0.1)

        try:
            r = requests.get('http://'+url+'/wp-content/plugins/'+plus)
            if r.status_code == 200:
                print(Fore.GREEN+" [+] "+Fore.WHITE+'http://'+url+'/wp-content/plugins/'+plus+" > "+Fore.GREEN+"Found")
    
            else:
                print(Fore.RED+" [-] "+Fore.WHITE+'http://'+url+'/wp-content/plugins/'+plus+" > "+Fore.RED+"Not Found")

        except:
            print("")
            sys.exit()

    input("\n"+Fore.BLUE+" [$] "+Fore.WHITE+"Back To Menu (Press Enter...) ")

def user():
    try:
        print(Fore.GREEN+" [+] "+Fore.WHITE+"Please Enter WordPress URL\n")
        print(Fore.YELLOW+" [!] "+Fore.WHITE+"Please Do Not Include Http\n")

        Url = input(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+"~"+Fore.RED+"@Root"+Fore.WHITE+"/"+"CMS Detection Woedperess"+"/"+"User"+Fore.GREEN+"""]
 └──╼  """+Fore.WHITE+"$ ").lower()

        s = requests.get("http://"+Url+"/wp-content/plugins/")

        if s.status_code == 404 or s.status_code == 500:
            print(Fore.YELLOW+" [!] "+Fore.WHITE+"Site NOT Wordpress")
            sys.exit()
        else:
            pass
        print(Fore.BLUE+" [*] "+"Please Wait . . .\n")
        time.sleep(0.5)

    except:
        print("")
        sys.exit()
    try:
        r = requests.get("https://"+Url+'/wp-json/wp/v2/users/').text
        j = json.loads(r)
        Count = len(j) - 1
        cn = 0
        User = ''

        for Val in j:
            Split = '\n'
            if Count == cn:
                Split = ''
            U = j[cn]['slug']
            if not U == '':
                User += Fore.GREEN+' [+] '+Fore.WHITE+U+Split
            cn += 1
        if User == '':
            User = Fore.RED+" [-] "+Fore.WHITE+'Not Found!'
        print (User+"\n")

        # else:
        #     print("User Not Found")

    except:
        print(Fore.YELLOW+" [!] "+Fore.WHITE+"ERROR ! ! \n"+"\n"+Fore.YELLOW+" [!] "+Fore.WHITE+"Please Enter The Valid Address\n"+"\n"+Fore.YELLOW+" [!] "+Fore.WHITE+"Or Plase Check Your Connection\n"+"\n"+Fore.YELLOW+" [!] "+Fore.WHITE+"Or I could not find the username\n ")
        sys.exit()
    try:
        input(Fore.BLUE+" [$] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()  