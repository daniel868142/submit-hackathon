"use strict";(self.webpackChunkui_react=self.webpackChunkui_react||[]).push([[3177],{4163:(t,r,n)=>{function e(t){return o.test(t)}n.d(r,{RH:()=>a,Qc:()=>E,Pz:()=>nt});var o=/^-?[0-9]+$/;function i(t){return c.test(t)}var c=/^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?$/;function a(t,r){var n=parseFloat(t),o=String(n),i=l(t),c=l(o);if(i===c)return!0;if(!0===(null==r?void 0:r.approx)){if(!e(t)&&c.length>=14&&i.startsWith(c.substring(0,14)))return!0}return!1}var u=function(t){return t.underflow="underflow",t.overflow="overflow",t.truncate_integer="truncate_integer",t.truncate_float="truncate_float",t}({});function f(t){if(!a(t,{approx:!1})){if(e(t))return u.truncate_integer;var r=parseFloat(t);return isFinite(r)?0===r?u.underflow:u.truncate_float:u.overflow}}function l(t){return t.replace(y,"").replace(v,"").replace(d,"").replace(s,"")}var y=/[eE][+-]?\d+$/,s=/^-?(0*)?/,v=/\./,d=/0+$/;function p(t){return p="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},p(t)}function h(t,r){for(var n=0;n<r.length;n++){var e=r[n];e.enumerable=e.enumerable||!1,e.configurable=!0,"value"in e&&(e.writable=!0),Object.defineProperty(t,b(e.key),e)}}function b(t){var r=function(t,r){if("object"!==p(t)||null===t)return t;var n=t[Symbol.toPrimitive];if(void 0!==n){var e=n.call(t,r||"default");if("object"!==p(e))return e;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===r?String:Number)(t)}(t,"string");return"symbol"===p(r)?r:String(r)}var m=function(){function t(r){if(function(t,r){if(!(t instanceof r))throw new TypeError("Cannot call a class as a function")}(this,t),function(t,r,n){(r=b(r))in t?Object.defineProperty(t,r,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[r]=n}(this,"isLosslessNumber",!0),!i(r))throw new Error('Invalid number (value: "'+r+'")');this.value=r}var r,n,o;return r=t,(n=[{key:"valueOf",value:function(){var t=f(this.value);if(void 0===t||t===u.truncate_float)return parseFloat(this.value);if(e(this.value))return BigInt(this.value);throw new Error("Cannot safely convert to number: "+"the value '".concat(this.value,"' would ").concat(t," and become ").concat(parseFloat(this.value)))}},{key:"toString",value:function(){return this.value}}])&&h(r.prototype,n),o&&h(r,o),Object.defineProperty(r,"prototype",{writable:!1}),t}();function w(t){return new m(t)}function S(t){return S="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},S(t)}function g(t,r,n,e){return Array.isArray(n)?e.call(t,r,function(t,r){for(var n=0;n<t.length;n++)t[n]=g(t,n+"",t[n],r);return t}(n,e)):n&&"object"===S(n)&&!function(t){return t&&"object"===p(t)&&!0===t.isLosslessNumber||!1}(n)?e.call(t,r,function(t,r){return Object.keys(t).forEach((function(n){var e=g(t,n,t[n],r);void 0!==e?t[n]=e:delete t[n]})),t}(n,e)):e.call(t,r,n)}function A(t){return A="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},A(t)}function C(t){return function(t){if(Array.isArray(t))return x(t)}(t)||function(t){if("undefined"!=typeof Symbol&&null!=t[Symbol.iterator]||null!=t["@@iterator"])return Array.from(t)}(t)||function(t,r){if(!t)return;if("string"==typeof t)return x(t,r);var n=Object.prototype.toString.call(t).slice(8,-1);"Object"===n&&t.constructor&&(n=t.constructor.name);if("Map"===n||"Set"===n)return Array.from(t);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return x(t,r)}(t)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function x(t,r){(null==r||r>t.length)&&(r=t.length);for(var n=0,e=new Array(r);n<r;n++)e[n]=t[n];return e}function E(t,r){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:w,e=0,o=a();return function(t){if(void 0===t)throw new SyntaxError("JSON value expected ".concat(x()))}(o),function(){if(e<t.length)throw new SyntaxError("Expected end of input ".concat(x()))}(),r?function(t,r){return g({"":t},"",t,r)}(o,r):o;function i(){if(t.charCodeAt(e)===J){e++,f();for(var r={},n=!0;e<t.length&&t.charCodeAt(e)!==P;){n?n=!1:(y(),f());var o=e,i=l();void 0===i&&p(),f(),s();var c=a();void 0===c&&S(),Object.prototype.hasOwnProperty.call(r,i)&&!k(c,r[i])&&h(i,o+1),r[i]=c}return t.charCodeAt(e)!==P&&function(){throw new SyntaxError("Quoted object key or end of object '}' expected ".concat(x()))}(),e++,r}}function c(){if(t.charCodeAt(e)===F){e++,f();for(var r=[],n=!0;e<t.length&&t.charCodeAt(e)!==$;){n?n=!1:y();var o=a();v(o),r.push(o)}return t.charCodeAt(e)!==$&&function(){throw new SyntaxError("Array item or end of array ']' expected ".concat(x()))}(),e++,r}}function a(){var r,o,a,y,s,v;f();var p=null!==(r=null!==(o=null!==(a=null!==(y=null!==(s=null!==(v=l())&&void 0!==v?v:function(){var r=e;t.charCodeAt(e)===H&&(e++,d(r));if(t.charCodeAt(e)===M)e++;else if(o=t.charCodeAt(e),o>=R&&o<=U)for(e++;O(t.charCodeAt(e));)e++;var o;if(t.charCodeAt(e)===q)for(e++,d(r);O(t.charCodeAt(e));)e++;if(t.charCodeAt(e)===Y||t.charCodeAt(e)===X)for(e++,t.charCodeAt(e)!==H&&t.charCodeAt(e)!==z||e++,d(r);O(t.charCodeAt(e));)e++;if(e>r)return n(t.slice(r,e))}())&&void 0!==s?s:i())&&void 0!==y?y:c())&&void 0!==a?a:u("true",!0))&&void 0!==o?o:u("false",!1))&&void 0!==r?r:u("null",null);return f(),p}function u(r,n){if(t.slice(e,e+r.length)===r)return e+=r.length,n}function f(){for(;(r=t.charCodeAt(e))===L||r===Q||r===T||r===B;)e++;var r}function l(){if(t.charCodeAt(e)===D){e++;for(var r="";e<t.length&&t.charCodeAt(e)!==D;){if(t.charCodeAt(e)===_){var n=t[e+1],o=I[n];void 0!==o?(r+=o,e++):"u"===n?j(t.charCodeAt(e+2))&&j(t.charCodeAt(e+3))&&j(t.charCodeAt(e+4))&&j(t.charCodeAt(e+5))?(r+=String.fromCharCode(parseInt(t.slice(e+2,e+6),16)),e+=5):A(e):m(e)}else(i=t.charCodeAt(e))>=32&&i<=1114111?r+=t[e]:b(t[e]);e++}return function(){if(t.charCodeAt(e)!==D)throw new SyntaxError("End of string '\"' expected ".concat(x()))}(),e++,r}var i}function y(){if(t.charCodeAt(e)!==W)throw new SyntaxError("Comma ',' expected after value ".concat(x()));e++}function s(){if(t.charCodeAt(e)!==G)throw new SyntaxError("Colon ':' expected after property name ".concat(x()));e++}function v(t){if(void 0===t)throw new SyntaxError("Array item expected ".concat(x()))}function d(r){if(!O(t.charCodeAt(e))){var n=t.slice(r,e);throw new SyntaxError("Invalid number '".concat(n,"', expecting a digit ").concat(x()))}}function p(){throw new SyntaxError("Quoted object key expected ".concat(x()))}function h(t,r){throw new SyntaxError("Duplicate key '".concat(t,"' encountered at position ").concat(r))}function b(t){throw new SyntaxError("Invalid character '".concat(t,"' ").concat(C()))}function m(r){var n=t.slice(r,r+2);throw new SyntaxError("Invalid escape character '".concat(n,"' ").concat(C()))}function S(){throw new SyntaxError("Object value expected after ':' ".concat(C()))}function A(r){for(var n=r+2;/\w/.test(t[n]);)n++;var e=t.slice(r,n);throw new SyntaxError("Invalid unicode character '".concat(e,"' ").concat(C()))}function C(){return"at position ".concat(e)}function x(){return(e<t.length?"but got '".concat(t[e],"'"):"but reached end of input")+" "+C()}}function j(t){return t>=M&&t<=U||t>=K&&t<=Z||t>=V&&t<=tt}function O(t){return t>=M&&t<=U}function k(t,r){return t===r||(Array.isArray(t)&&Array.isArray(r)?t.length===r.length&&t.every((function(t,n){return k(t,r[n])})):!(!N(t)||!N(r))&&C(new Set([].concat(C(Object.keys(t)),C(Object.keys(r))))).every((function(n){return k(t[n],r[n])})))}function N(t){return"object"===A(t)&&null!==t}var I={'"':'"',"\\":"\\","/":"/",b:"\b",f:"\f",n:"\n",r:"\r",t:"\t"},_=92,J=123,P=125,F=91,$=93,L=32,Q=10,T=9,B=13,D=34,z=43,H=45,M=48,R=49,U=57,W=44,q=46,G=58,K=65,V=97,X=69,Y=101,Z=70,tt=102;function rt(t){return rt="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},rt(t)}function nt(t,r,n,e){var o=function(t){if("number"==typeof t)return" ".repeat(t);if("string"==typeof t&&""!==t)return t;return}(n);return c("function"==typeof r?r.call({"":t},"",t):t,"");function c(t,a){if(Array.isArray(e)){var u=e.find((function(r){return r.test(t)}));if(u){var f=u.stringify(t);if("string"!=typeof f||!i(f))throw new Error("Invalid JSON number: output of a number stringifier must be a string containing a JSON number "+"(output: ".concat(f,")"));return f}}return"boolean"==typeof t||"number"==typeof t||"string"==typeof t||null===t||t instanceof Date||t instanceof Boolean||t instanceof Number||t instanceof String?JSON.stringify(t):t&&t.isLosslessNumber||"bigint"==typeof t?t.toString():Array.isArray(t)?function(t,n){if(0===t.length)return"[]";for(var e=o?n+o:void 0,i=o?"[\n":"[",a=0;a<t.length;a++){var u="function"==typeof r?r.call(t,String(a),t[a]):t[a];o&&(i+=e),i+=void 0!==u&&"function"!=typeof u?c(u,e):"null",a<t.length-1&&(i+=o?",\n":",")}return i+=o?"\n"+n+"]":"]",i}(t,a):t&&"object"===rt(t)?function(t,e){if("function"==typeof t.toJSON)return nt(t.toJSON(),r,n,void 0);var i=Array.isArray(r)?r.map(String):Object.keys(t);if(0===i.length)return"{}";var a=o?e+o:void 0,u=!0,f=o?"{\n":"{";return i.forEach((function(n){var e="function"==typeof r?r.call(t,n,t[n]):t[n];if(function(t,r){return void 0!==r&&"function"!=typeof r&&"symbol"!==rt(r)}(0,e)){u?u=!1:f+=o?",\n":",";var i=JSON.stringify(n);f+=o?a+i+": ":i+":",f+=c(e,a)}})),f+=o?"\n"+e+"}":"}",f}(t,a):void 0}}}}]);