#!/usr/bin/python

# Ubuntu Tweak - PyGTK based desktop configure tool
#
# Copyright (C) 2007-2008 TualatriX <tualatrix@gmail.com>
#
# Ubuntu Tweak is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ubuntu Tweak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ubuntu Tweak; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

import os
import gtk
from consts import *

__all__ = (
    'get_app_describ',
    'get_source_describ',
    'get_app_logo',
    'get_source_logo',
)

def get_app_describ(name):
    name = name.replace(' ', '-').lower()
    try:
        desc = APP_DICT[name]
    except KeyError:
        desc = 'Unknown Error'

    return desc

def get_source_describ(name):
    name = name.replace(' ', '-').lower()
    try:
        desc = SOURCE_DICT[name]
    except KeyError:
        desc = get_app_describ(name)

    return desc

def get_app_logo(name, size=32):
    try:
        name = '%s.png' % name.replace(' ', '-').lower()
        path = os.path.join(DATA_DIR, 'applogos', name)

        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        if pixbuf.get_width() != size or pixbuf.get_height() != size:
            pixbuf = pixbuf.scale_simple(size, size, gtk.gdk.INTERP_BILINEAR)
        return pixbuf
    except:
        icon = gtk.icon_theme_get_default()
        return icon.load_icon(gtk.STOCK_MISSING_IMAGE, size, 0)

def get_source_logo(name):
    return get_app_logo(name)

APP_DICT = {
    'agave': _('A color scheme designer'),
    'amarok-nightly': _('Development version of an audio player for KDE'),
    'amule': _('Client for the eD2k and Kad networks'),
    'anjuta': _('GNOME IDE for C/C++, Java, Python'),
    'arc-colors': _('Arc-Colors is a set of wallpapers and GDM themes made to complement the Shiki-Colors GTK+ themes and the GNOME-Colors icon themes.'),
    'audacious': _('A skinned multimedia player for many platforms'),
    'audacity': _('Record and edit audio files'),
    'avant-window-navigator': _('Fully customisable dock-like window navigator'),
    'avant-window-navigator-trunk': _('Fully customisable dock-like window navigator(Unstable)'),
    'avidemux': _('A free video editor'),
    'azureus': _('BitTorrent client written in Java'),
    'banshee': _('Audio Management and Playback application'),
    'blueman': _('GTK+ Bluetooth Manager'),
    'backintime-gnome': _('Simple backup system for GNOME Desktop'),
    'backintime-kde4': _('Simple backup system for KDE4 Desktop'),
    'breathe-icon-theme': _("The Breathe icon theme is a refresh of the Human icon theme using KDE's Oxygen icon set as an inspiration but with that distinctly Human feel."),
    'cairo-dock': _('A true dock for linux'),
    'chmsee': _('A chm file viewer written in GTK+'),
    'christine': _('Desired to be small and fast, christine is a simple media player, that let you play your favorite music and videos from one single application.'),
    'chromium-browser': _('Chromium is an open-source browser project that aims to build a safer, faster, and more stable way for all Internet users to experience the web.'),
    'codeblocks': _('The open source, cross-platform IDE'),
    'compizconfig-settings-manager': _('Advanced Desktop Effects Settings Manager'),
    'devhelp': _('An API documentation browser for GNOME.'),
    'deluge-torrent': _('A Bittorrent client written in PyGTK'),
    'nautilus-dropbox': _('Store, Sync and Share your files online.'),
    'eclipse': _('Extensible Tool Platform and Java IDE'),
    'eioffice-personal': _('EIOffice Personal 2009. Free for Chinese users. See http://www.evermoresw.com.'),
    'emesene': _('A client for the Windows Live Message network'),
    'empathy': _('Empathy consists of a rich set of reusable instant messaging widgets, and a GNOME client using those widgets.'),
    'exaile': _('flexible audio player, similar to Amarok, but written in GTK+'),
    'filezilla': _('File transmission via ftp, sftp and ftps'),
    'pcmanfm': _('An extremly fast and lightweight file manager'),
    'galaxium': _('Galaxium is an instant messenger application designed for the GNOME desktop'),
    'gajim': _('A GTK+ jabber client'),
    'geany': _('A fast and lightweight IDE'),
    'gftp': _('A multithreaded FTP client'),
    'ghex': _('GNOME Hex editor'),
    'gloobus-preview': _('Gloobus is an extension of Gnome designed to enable a full screen preview of any kind of file.'),
    'gimp': _('The GNU Image Manipulation Program'),
    'giver': _('A simple file sharing desktop application'),
    'gmail-notify': _('Notifies the user upon arrival of new mail in Gmail'),
    'gmchess': _('GMChess is chinese chess game write by gtkmm'),
    'gnome-do': _('A powerful, speedy, and sexy remote control for the GNOME Desktop'),
    'gnome-do-plugins': _('Extra functionality for GNOME-Do launcher'),
    'gnome-globalmenu': _('Global Menu Bar for GNOME'),
    'gnome-colors': _('GNOME-Colors is a set of GNOME icon themes, with some inspiration from Tango, Elementary, Discovery, Tango Generator and others.'),
    'gnote': _('a C++ port of Tomboy'),
    'googleearth': _("A program that combines satellite imagery and maps to put the world's geographic information at your fingertips."),
    'google-gadgets': _('Platform for running Google Gadgets on Linux'),
    'google-chrome-unstable': _('Google Chrome is a browser that combines a minimal design with sophisticated technology to make the web faster, safer, and easier.'),
    'gparted': _('GNOME partition editor'),
    'gpicview': _('Lightweight image viewer'),
    'gtk-recordmydesktop': _('Graphical frontend for recordmydesktop'),
    'gtg': _('GTG is a personal organizer for the GNOME desktop environment, it focuses on ease of use and flexibility, while keeping things simple.'),
    'gwibber': _('Gwibber is an open source microblogging client for GNOME'),
    'isomaster': _('A graphical CD image editor'),
    'ibus': _('Intelligent Input Bus for Linux / Unix OS'),
    'ibus-pinyin': _('It is a PinYin engine for IBus.'),
    'ibus-table': _('IBus-Table is the IM Engine framework for table-based input methods, such as ZhengMa, WuBi, ErBi, ChangJie and so on.'),
    'ibus-table-wubi': _('Wubi input method based on table engine of ibus'),
    'inkscape': _('Create and edit Scalable Vector Graphics images'),
    'inkscape-devel': _('Create and edit Scalable Vector Graphics images'),
    'kino': _('Non-linear editor for Digital Video data'),
    'lastfm': _('A music player for Last.fm personalized radio'),
    'leafpad': _('GTK+ based simple text editor'),
    'liferea': _('Feed aggregator for GNOME'),
    'mail-notification': _('Mail notification in system tray'),
    'meld': _('Adcal tool to diff and merge files'),
    'mirage': _('A fast and simple GTK+ Image Viewer'),
    'miro': _('Open internet TV, beyond anything else'),
    'midori': _('Webkit based lightweight web browser'),
    'moovida': _('The free media player - play all your files'),
    'monodevelop': _('An IDE to Develop .NET applications.'),
    'moblin': _('A moblin feature enabled environment for Ubuntu (Testing Only)'),
    'mplayer': _('The Ultimate Movie Player For Linux'),
    'netbeans': _('IDE for Java, C/C++, Ruby, UML, etc.'),
    'opera': _('The Opera Web Browser'),
    'pidgin': _('Pidgin is a graphical modular messaging client based on libpurple which is capable of connecting to AIM, MSN, Yahoo!, XMPP, ICQ, IRC, SILC, SIP/SIMPLE, Novell GroupWise, Lotus Sametime, Bonjour, Zephyr, MySpaceIM, Gadu-Gadu, and QQ all at once.'),
    'playonlinux': _('PlayOnLinux is a front-end for wine. It permits you to install Windows Games and softwares on Linux.'),
    'picasa': _('Image management application from Google'),
    'qt-creator': _('IDE for Development with Qt'),
    'rednotebook': _('RedNotebook is a graphical diary and journal to keep track of notes and thoughts throughout the day. It includes a calendar navigation, customisable templates for each day, and a keyword search and cloud.'),
    'shiki-colors': _('Shiki-Colors is a set of Metacity/GTK-2+ themes which mix the elegance of a dark theme with the usability of a light theme, resulting in a hybrid theme.'),
    'screenlets': _('A framework for desktop widgets'),
    'shutter': _('Feature-rich screenshot application(formerly known as GScrot)'),
    'skype': _('Make audio/video calls using this VoIP Software'),
    'smplayer': _('A great MPlayer front-end, written in QT4'),
    'soundconverter': _('Convert audio files into other formats'),
    'spicebird': _('A fully integrated mail, PIM and instant messaging client'),
    'stardict': _('An international dictionary'),
    'swiftweasel': _('Swiftweasel is an optimized build of the Mozilla Firefox web browser for Linux'),
    'specto': _('A desktop application that will watch for events (website updates, emails, file and folder changes...)'),
    'synapse': _('An instant messaging application powered by qt-mono-bindings'),
    'tasque': _('A Useful Task List'),
    'terminator': _('Multiple GNOME terminals in one window'),
    'transmission-gtk': _('Transmission is a fast, easy, and free multi-platform BitTorrent client.'),
    'ubuntu-tweak': _('Ubuntu Tweak makes it easier to configure Ubuntu'),
    'ubuntu-restricted-extras': _('Commonly used restricted packages'),
    'ubudsl': _('configure your USB ADSL modem and connection easier than ever!'),
    'virtualbox': _('A feature rich, high performance virtualization software'),
    'virtualbox-3.0': _('A feature rich, high performance virtualization software'),
    'virtualbox-ose': _('A feature rich, high performance virtualization software'),
    'vlc': _('Read, capture, broadcast your multimedia streams'),
    'vmware-player': _('Run Virtual Machines using VMware'),
    'wine': _('A compatibility layer for running Windows programs'),
    'wine-doors': _('Wine-doors is an application designed to make installing windows software on Linux, Solaris or other Unix systems easier.'),
    'xbmc': _('XBMC is a free and open source software media player and entertainment hub'),
    'zim': _('Zim is a WYSIWYG text editor. It aims at bringing the concept of a wiki to your desktop.'),
    'step-into-freedom-theme': _('Step-into-freedom theme contains a full theme for GNOME based system.'),
    'ubuntu-sunrise-theme': _('Ubuntu-sunrise theme contains a full theme for GNOME based system.'),
    'bamboo-zen-theme': _('Bamboo-zen theme contains a full theme for GNOME based system.'),
    'exotic-theme': _('Exotic theme contains a full theme for GNOME based system.'),
    'aquadreams-theme': _('Aquadreams theme contains a full theme for GNOME based system.'),
    'showtime-theme': _('Showtime theme contains a full theme for GNOME based system.'),
    'infinity-theme': _('Infinity theme contains a full theme for GNOME based system.'),
    'tropical-theme': _('Tropical theme contains a full theme for GNOME based system.'),
    'wild-shine-theme': _('Wild-shine theme contains a full theme for GNOME based system.'),
    'balanzan-theme': _('Balanzan theme contains a full theme for GNOME based system.'),
    'dia': _('Dia is an editor for diagrams, graphs, charts etc.'),
    'pitivi': _('non-linear audio/video editor using GStreamer'),
    'lyx': _('LyX is an almost WYSIWYG-frontend for LaTeX.'),
    'texmaker': _('Texmaker is a clean, highly configurable LaTeX editor with good hot key support and extensive LaTeX documentation.'),
    'tomboy': _('Tomboy is a desktop note-taking application which is simple and easy to use.'),
    'pdfmod': _('PDF Mod is a simple tool for modifying PDF documents.'),
    'osdlyrics': _('An OSD lyrics show compatible with various media players.'),
    'openshot': _('OpenShot Video Editor is a free, open-source, non-linear video editor, based on Python, GTK, and MLT.'),
}

SOURCE_DICT = {
    'firefox': _('Development Version of Mozilla Firefox'),
    'compiz': _('Development version of Compiz'),
    'google': _("Google's Linux Repository"),
    'kde-4': _('Development Version of K Desktop Environment'),
    'lxde': _('Lightweight X11 Desktop Environment: GPicView, PCManFM'),
    'webkitgtk': _('WebkitGtk+, Liferea (Webkit), Midori and other WebKit related projects.'),
    'medibuntu': _('Multimedia, Entertainment and Distraction In Ubuntu\nMedibuntu is a repository of packages that cannot be included into the Ubuntu distribution for legal reasons (copyright, license, patent, etc).'),
    'openoffice': 'OpenOffice.org 3.1 for Ubuntu',
    'ubuntu-cn': _('Ubuntu repository for Chinese users.\n'
        'Including EIOffice, Ubuntu Tweak, ibus input method, OpenOffice.org 3.0 and other softwares.'),
    'getdeb': _('GetDeb extends the existing software options for Ubuntu (and derived) Linux distributions by providing major updates and software not yet available on the official Ubuntu repositories.'),
    'ubuntu-x': _('Updated versions of X.org drivers, libraries, etc. for Ubuntu.'),
    'gnome-games': _('Gnome Games built from Git, with all experimental features and staging games enabled.'),
    'mozilla-security': _('Ubuntu Mozilla Security Team provides beta and final stable/security updates for mozilla software in its PPA'),
    'qt': _('A cross-platform application and UI framework'),
    'mono': _('Mono is a cross platform, open source .NET development framework.'),
    'clutter': _('Clutter is an OpenGL based interactive canvas library, designed for creating fast, mainly 2D single window applications such as media box UIs, presentations, kiosk style applications and so on.'),
    'gloobus': _('Gloobus is an extension of Gnome designed to enable a full screen preview of any kind of file.'),
    'bisigi': _('Behind this African word, referring to the notion of imagination, you can find some themes for GNOME'),
    'kubuntu-update': _('Updates for Kubuntu releases which are due to go to Ubuntu Updates. Mostly KDE point releases.'),
    'kubuntu-backports': _('Backports of new versions of KDE for Kubuntu which are not yet tested enough to go to Ubuntu Backports.'),
}

P2P = (_('File-Sharing Clients'), 'p2p.png')
Image = (_('Image Tools'), 'image.png')
Sound = (_('Sound Tools'), 'sound.png')
Video = (_('Video Tools'), 'video.png')
Text = (_('Text Tools'), 'text.png')
IM = (_('Instant Messengers'), 'im.png')
Internet = (_('Internet Tools'), 'internet.png')
FTP = (_('FTP Tools'), 'ftp.png')
Desktop = (_('Desktop Tools'), 'desktop.png')
Disk = (_('CD/Disk Tools'), 'cd.png')
Develop = (_('Development'), 'develop.png')
Emulator = (_('Emulators'), 'emulator.png')
Theme = (_('Themes'), 'theme.png')
Mail = (_('E-mail Tools'), 'mail.png')

def create_cate(*items):
    new = []
    for i, item in enumerate(items):
        list = [i]
        list.extend(item)
        new.append(list)
    return new

CATES_DATA = create_cate(P2P, Image, Sound, Video, Text, IM, Internet, FTP, Desktop, Disk, Develop, Emulator, Theme, Mail)

APPS = \
{
    'agave': Image,
    'amule': P2P,
    'amarok-nightly': Sound,
    'anjuta': Develop,
    'audacious': Sound,
    'audacity': Sound,
    'avant-window-navigator': Desktop,
    'avant-window-navigator-trunk': Desktop,
    'avidemux': Video,
    'azureus': P2P,
    'banshee': Sound,
    'blueman': P2P,
    'backintime-gnome': Desktop,
    'backintime-kde4': Desktop,
    'breathe-icon-theme': Theme,
    'cairo-dock': Desktop,
    'chmsee': Text,
    'christine': Sound,
    'chromium-browser': Internet,
    'compizconfig-settings-manager': Desktop,
    'codeblocks': Develop,
    'devhelp': Develop,
    'deluge-torrent': P2P,
    'eclipse': Develop,
    'emesene': IM,
    'empathy': IM,
    'eioffice-personal': Text,
    'exaile': Sound,
    'filezilla': FTP,
    'pcmanfm': Desktop,
    'gimp': Image,
    'gloobus-preview': Desktop,
    'giver': P2P,
    'galaxium': IM,
    'gajim': IM,
    'geany': Develop,
    'gftp': FTP,
    'ghex': Text,
    'gmail-notify': Mail,
    'gnote': Text,
    'gnome-do': Desktop,
    'gnome-do-plugins': Desktop,
    'gnome-globalmenu': Desktop,
    'gnome-colors': Theme,
    'shiki-colors': Theme,
    'arc-colors': Theme,
    'googleearth': Internet,
    'google-gadgets': Desktop,
    'google-chrome-unstable': Internet,
    'gparted': Disk,
    'gpicview': Image,
    'gtk-recordmydesktop': Video,
    'gwibber': Internet,
    'gtg': Text,
    'isomaster': Disk,
    'inkscape': Image,
    'inkscape-devel': Image,
    'ibus-pinyin': Text,
    'ibus-table-wubi': Text,
    'kino': Video,
    'lastfm': Internet,
    'leafpad': Text,
    'liferea': Internet,
    'mail-notification': Mail,
    'meld': Text,
    'mirage': Image,
    'miro': Video,
    'midori': Internet,
    'moovida': Sound,
    'monodevelop': Develop,
    'mplayer': Video,
    'netbeans': Develop,
    'nautilus-dropbox': Internet,
    'opera': Internet,
    'playonlinux': Emulator,
    'picasa': Image,
    'qt-creator': Develop,
    'rednotebook': Text,
    'screenlets': Desktop,
    'specto': Desktop,
    'shutter': Image,
    'skype': IM,
    'smplayer': Video,
    'soundconverter': Sound,
    'stardict': Desktop,
    'synapse': IM,
    'spicebird': Internet,
    'tasque': Desktop,
    'terminator': Emulator,
    'transmission-gtk': P2P,
    'ubudsl': Internet,
    'ubuntu-restricted-extras': Desktop,
    'virtualbox-ose': Emulator,
    'virtualbox-3.0': Emulator,
    'vlc': Video,
    'vmware-player': Emulator,
    'wine': Emulator,
    'wine-doors': Emulator,
    'xbmc': Desktop,
    'zim': Text,
    'step-into-freedom-theme': Theme,
    'ubuntu-sunrise-theme': Theme,
    'bamboo-zen-theme': Theme,
    'exotic-theme': Theme,
    'aquadreams-theme': Theme,
    'showtime-theme': Theme,
    'infinity-theme': Theme,
    'tropical-theme': Theme,
    'wild-shine-theme': Theme,
    'balanzan-theme': Theme,
    'dia': Image,
    'pitivi': Video,
    'lyx': Text,
    'texmaker': Text,
    'tomboy': Text,
    'pdfmod': Text,
    'osdlyrics': Sound,
    'openshot': Video,
}

if __name__ == '__main__':
    print get_app_describ('Avant Window Navigator')
    print get_app_describ('Banshee')
    print get_source_describ('wine')
