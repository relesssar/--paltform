!function(e,t){for(var n in t)e[n]=t[n]}(window,webpackJsonp([45],{"./lms/static/js/accessible_components/StatusBarAlert.jsx":function(e,t,n){"use strict";function r(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}Object.defineProperty(t,"__esModule",{value:!0}),n.d(t,"StatusAlertRenderer",function(){return l});var s=n("./node_modules/react/index.js"),o=n.n(s),i=n("./node_modules/react-dom/index.js"),a=n.n(i),c=n("./node_modules/@edx/paragon/static/index.js"),u=(n.n(c),function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}()),l=function(){function e(t,n,s){var i=this;r(this,e),this.shiftFocus=this.shiftFocus.bind(this),document.querySelector(n)&&a.a.render(o.a.createElement(c.StatusAlert,{alertType:"warning",dismissible:!0,open:!0,dialog:t,dismissable:!0,onClose:function(){return i.shiftFocus(s)}}),document.querySelector(n))}return u(e,[{key:"shiftFocus",value:function(e){var t=document.querySelector(e);t&&t.focus()}}]),e}()}},["./lms/static/js/accessible_components/StatusBarAlert.jsx"]));