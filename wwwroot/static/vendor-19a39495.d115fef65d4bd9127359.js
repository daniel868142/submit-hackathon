"use strict";(self.webpackChunkui_react=self.webpackChunkui_react||[]).push([[5860],{69103:(e,t,n)=>{n.d(t,{$h:()=>o,Tx:()=>u,ZC:()=>i,ht:()=>s});var r=n(9488);const s=(e,t)=>e===t;function i(e=s){return(t,n)=>r.fS(t,n,e)}function o(){return(e,t)=>e.equals(t)}function u(e,t,n){return e&&t?n(e,t):e===t}new WeakMap},59523:(e,t,n)=>{n.d(t,{y:()=>a});var r=n(9488),s=n(98401),i=n(63580);function o(e,t){return t&&(e.stack||e.stacktrace)?i.NC("stackTrace.format","{0}: {1}",l(e),u(e.stack)||u(e.stacktrace)):l(e)}function u(e){return Array.isArray(e)?e.join("\n"):e}function l(e){return"ERR_UNC_HOST_NOT_ALLOWED"===e.code?`${e.message}. Please update the 'security.allowedUNCHosts' setting if you want to allow this host.`:"string"==typeof e.code&&"number"==typeof e.errno&&"string"==typeof e.syscall?i.NC("nodeExceptionMessage","A system error occurred ({0})",e.message):e.message||i.NC("error.defaultMessage","An unknown error occurred. Please consult the log for more details.")}function a(e=null,t=!1){if(!e)return i.NC("error.defaultMessage","An unknown error occurred. Please consult the log for more details.");if(Array.isArray(e)){const n=r.kX(e),s=a(n[0],t);return n.length>1?i.NC("error.moreErrors","{0} ({1} errors in total)",s,n.length):s}if(s.HD(e))return e;if(e.detail){const n=e.detail;if(n.error)return o(n.error,t);if(n.exception)return o(n.exception,t)}return e.stack?o(e,t):e.message?e.message:i.NC("error.defaultMessage","An unknown error occurred. Please consult the log for more details.")}},17301:(e,t,n)=>{n.d(t,{B8:()=>f,Cp:()=>i,F0:()=>c,FU:()=>a,L6:()=>d,b1:()=>h,dL:()=>s,he:()=>p,n2:()=>l,ri:()=>o});const r=new class{constructor(){this.listeners=[],this.unexpectedErrorHandler=function(e){setTimeout((()=>{if(e.stack){if(v.isErrorNoTelemetry(e))throw new v(e.message+"\n\n"+e.stack);throw new Error(e.message+"\n\n"+e.stack)}throw e}),0)}}emit(e){this.listeners.forEach((t=>{t(e)}))}onUnexpectedError(e){this.unexpectedErrorHandler(e),this.emit(e)}onUnexpectedExternalError(e){this.unexpectedErrorHandler(e)}};function s(e){l(e)||r.onUnexpectedError(e)}function i(e){l(e)||r.onUnexpectedExternalError(e)}function o(e){if(e instanceof Error){const{name:t,message:n}=e;return{$isError:!0,name:t,message:n,stack:e.stacktrace||e.stack,noTelemetry:v.isErrorNoTelemetry(e)}}return e}const u="Canceled";function l(e){return e instanceof a||e instanceof Error&&e.name===u&&e.message===u}class a extends Error{constructor(){super(u),this.name=this.message}}function c(){const e=new Error(u);return e.name=e.message,e}function h(e){return e?new Error(`Illegal argument: ${e}`):new Error("Illegal argument")}function d(e){return e?new Error(`Illegal state: ${e}`):new Error("Illegal state")}class f extends Error{constructor(e){super("NotSupported"),e&&(this.message=e)}}class v extends Error{constructor(e){super(e),this.name="CodeExpectedError"}static fromError(e){if(e instanceof v)return e;const t=new v;return t.message=e.message,t.stack=e.stack,t}static isErrorNoTelemetry(e){return"CodeExpectedError"===e.name}}class p extends Error{constructor(e){super(e||"An unexpected bug occurred."),Object.setPrototypeOf(this,p.prototype)}}},4669:(e,t,n)=>{n.d(t,{D0:()=>w,E7:()=>k,K3:()=>L,Q5:()=>g,SZ:()=>E,Sp:()=>_,ZD:()=>A,ju:()=>l,z5:()=>C});var r=n(17301),s=n(88289),i=n(5976),o=n(91741),u=n(84013);var l;!function(e){function t(e){false}function n(e){return(t,n=null,r)=>{let s,i=!1;return s=e((e=>{if(!i)return s?s.dispose():i=!0,t.call(n,e)}),null,r),i&&s.dispose(),s}}function r(e,t,n){return o(((n,r=null,s)=>e((e=>n.call(r,t(e))),null,s)),n)}function s(e,t,n){return o(((n,r=null,s)=>e((e=>t(e)&&n.call(r,e)),null,s)),n)}function o(e,n){let r;const s={onWillAddFirstListener(){r=e(i.fire,i)},onDidRemoveLastListener(){null==r||r.dispose()}};n||t();const i=new g(s);return null==n||n.add(i),i.event}function u(e,n,r=100,s=!1,i=!1,o,u){let l,a,c,h,d=0;const f={leakWarningThreshold:o,onWillAddFirstListener(){l=e((e=>{d++,a=n(a,e),s&&!c&&(v.fire(a),a=void 0),h=()=>{const e=a;a=void 0,c=void 0,(!s||d>1)&&v.fire(e),d=0},"number"==typeof r?(clearTimeout(c),c=setTimeout(h,r)):void 0===c&&(c=0,queueMicrotask(h))}))},onWillRemoveListener(){i&&d>0&&(null==h||h())},onDidRemoveLastListener(){h=void 0,l.dispose()}};u||t();const v=new g(f);return null==u||u.add(v),v.event}e.None=()=>i.JT.None,e.defer=function(e,t){return u(e,(()=>{}),0,void 0,!0,void 0,t)},e.once=n,e.map=r,e.forEach=function(e,t,n){return o(((n,r=null,s)=>e((e=>{t(e),n.call(r,e)}),null,s)),n)},e.filter=s,e.signal=function(e){return e},e.any=function(...e){return(t,n=null,r)=>function(e,t){t instanceof Array?t.push(e):t&&t.add(e);return e}((0,i.F8)(...e.map((e=>e((e=>t.call(n,e)))))),r)},e.reduce=function(e,t,n,s){let i=n;return r(e,(e=>(i=t(i,e),i)),s)},e.debounce=u,e.accumulate=function(t,n=0,r){return e.debounce(t,((e,t)=>e?(e.push(t),e):[t]),n,void 0,!0,void 0,r)},e.latch=function(e,t=(e,t)=>e===t,n){let r,i=!0;return s(e,(e=>{const n=i||!t(e,r);return i=!1,r=e,n}),n)},e.split=function(t,n,r){return[e.filter(t,n,r),e.filter(t,(e=>!n(e)),r)]},e.buffer=function(e,t=!1,n=[],r){let s=n.slice(),i=e((e=>{s?s.push(e):u.fire(e)}));r&&r.add(i);const o=()=>{null==s||s.forEach((e=>u.fire(e))),s=null},u=new g({onWillAddFirstListener(){i||(i=e((e=>u.fire(e))),r&&r.add(i))},onDidAddFirstListener(){s&&(t?setTimeout(o):o())},onDidRemoveLastListener(){i&&i.dispose(),i=null}});return r&&r.add(u),u.event},e.chain=function(e,t){return(n,r,s)=>{const i=t(new a);return e((function(e){const t=i.evaluate(e);t!==l&&n.call(r,t)}),void 0,s)}};const l=Symbol("HaltChainable");class a{constructor(){this.steps=[]}map(e){return this.steps.push(e),this}forEach(e){return this.steps.push((t=>(e(t),t))),this}filter(e){return this.steps.push((t=>e(t)?t:l)),this}reduce(e,t){let n=t;return this.steps.push((t=>(n=e(n,t),n))),this}latch(e=(e,t)=>e===t){let t,n=!0;return this.steps.push((r=>{const s=n||!e(r,t);return n=!1,t=r,s?r:l})),this}evaluate(e){for(const t of this.steps)if((e=t(e))===l)break;return e}}e.fromNodeEventEmitter=function(e,t,n=e=>e){const r=(...e)=>s.fire(n(...e)),s=new g({onWillAddFirstListener:()=>e.on(t,r),onDidRemoveLastListener:()=>e.removeListener(t,r)});return s.event},e.fromDOMEventEmitter=function(e,t,n=e=>e){const r=(...e)=>s.fire(n(...e)),s=new g({onWillAddFirstListener:()=>e.addEventListener(t,r),onDidRemoveLastListener:()=>e.removeEventListener(t,r)});return s.event},e.toPromise=function(e){return new Promise((t=>n(e)(t)))},e.fromPromise=function(e){const t=new g;return e.then((e=>{t.fire(e)}),(()=>{t.fire(void 0)})).finally((()=>{t.dispose()})),t.event},e.runAndSubscribe=function(e,t,n){return t(n),e((e=>t(e)))};class c{constructor(e,n){this._observable=e,this._counter=0,this._hasChanged=!1;const r={onWillAddFirstListener:()=>{e.addObserver(this)},onDidRemoveLastListener:()=>{e.removeObserver(this)}};n||t(),this.emitter=new g(r),n&&n.add(this.emitter)}beginUpdate(e){this._counter++}handlePossibleChange(e){}handleChange(e,t){this._hasChanged=!0}endUpdate(e){this._counter--,0===this._counter&&(this._observable.reportChanges(),this._hasChanged&&(this._hasChanged=!1,this.emitter.fire(this._observable.get())))}}e.fromObservable=function(e,t){return new c(e,t).emitter.event},e.fromObservableLight=function(e){return(t,n,r)=>{let s=0,o=!1;const u={beginUpdate(){s++},endUpdate(){s--,0===s&&(e.reportChanges(),o&&(o=!1,t.call(n)))},handlePossibleChange(){},handleChange(){o=!0}};e.addObserver(u),e.reportChanges();const l={dispose(){e.removeObserver(u)}};return r instanceof i.SL?r.add(l):Array.isArray(r)&&r.push(l),l}}}(l||(l={}));class a{constructor(e){this.listenerCount=0,this.invocationCount=0,this.elapsedOverall=0,this.durations=[],this.name=`${e}_${a._idPool++}`,a.all.add(this)}start(e){this._stopWatch=new u.G,this.listenerCount=e}stop(){if(this._stopWatch){const e=this._stopWatch.elapsed();this.durations.push(e),this.elapsedOverall+=e,this.invocationCount+=1,this._stopWatch=void 0}}}a.all=new Set,a._idPool=0;class c{constructor(e,t,n=Math.random().toString(18).slice(2,5)){this._errorHandler=e,this.threshold=t,this.name=n,this._warnCountdown=0}dispose(){var e;null===(e=this._stacks)||void 0===e||e.clear()}check(e,t){const n=this.threshold;if(n<=0||t<n)return;this._stacks||(this._stacks=new Map);const r=this._stacks.get(e.value)||0;if(this._stacks.set(e.value,r+1),this._warnCountdown-=1,this._warnCountdown<=0){this._warnCountdown=.5*n;const[e,r]=this.getMostFrequentStack(),s=`[${this.name}] potential listener LEAK detected, having ${t} listeners already. MOST frequent listener (${r}):`,i=new d(s,e);this._errorHandler(i)}return()=>{const t=this._stacks.get(e.value)||0;this._stacks.set(e.value,t-1)}}getMostFrequentStack(){if(!this._stacks)return;let e,t=0;for(const[n,r]of this._stacks)(!e||t<r)&&(e=[n,r],t=r);return e}}class h{static create(){var e;const t=new Error;return new h(null!==(e=t.stack)&&void 0!==e?e:"")}constructor(e){this.value=e}print(){}}class d extends Error{constructor(e,t){super(e),this.name="ListenerLeakError",this.stack=t}}class f extends Error{constructor(e,t){super(e),this.name="ListenerRefusalError",this.stack=t}}class v{constructor(e){this.value=e}}const p=void 0;class g{constructor(e){var t,n,s,i,o,u;this._size=0,this._options=e,this._leakageMon=(null===(t=this._options)||void 0===t?void 0:t.leakWarningThreshold)?new c(null!==(n=null==e?void 0:e.onListenerError)&&void 0!==n?n:r.dL,null!==(i=null===(s=this._options)||void 0===s?void 0:s.leakWarningThreshold)&&void 0!==i?i:-1):void 0,this._perfMon=(null===(o=this._options)||void 0===o?void 0:o._profName)?new a(this._options._profName):void 0,this._deliveryQueue=null===(u=this._options)||void 0===u?void 0:u.deliveryQueue}dispose(){var e,t,n,r;this._disposed||(this._disposed=!0,(null===(e=this._deliveryQueue)||void 0===e?void 0:e.current)===this&&this._deliveryQueue.reset(),this._listeners&&(this._listeners=void 0,this._size=0),null===(n=null===(t=this._options)||void 0===t?void 0:t.onDidRemoveLastListener)||void 0===n||n.call(t),null===(r=this._leakageMon)||void 0===r||r.dispose())}get event(){var e;return null!==(e=this._event)&&void 0!==e||(this._event=(e,t,n)=>{var s,o,u,l,a,c,d;if(this._leakageMon&&this._size>this._leakageMon.threshold**2){const e=`[${this._leakageMon.name}] REFUSES to accept new listeners because it exceeded its threshold by far (${this._size} vs ${this._leakageMon.threshold})`,t=null!==(s=this._leakageMon.getMostFrequentStack())&&void 0!==s?s:["UNKNOWN stack",-1],n=new f(`${e}. HINT: Stack shows most frequent listener (${t[1]}-times)`,t[0]);return((null===(o=this._options)||void 0===o?void 0:o.onListenerError)||r.dL)(n),i.JT.None}if(this._disposed)return i.JT.None;t&&(e=e.bind(t));const g=new v(e);let _;this._leakageMon&&this._size>=Math.ceil(.2*this._leakageMon.threshold)&&(g.stack=h.create(),_=this._leakageMon.check(g.stack,this._size+1)),this._listeners?this._listeners instanceof v?(null!==(d=this._deliveryQueue)&&void 0!==d||(this._deliveryQueue=new m),this._listeners=[this._listeners,g]):this._listeners.push(g):(null===(l=null===(u=this._options)||void 0===u?void 0:u.onWillAddFirstListener)||void 0===l||l.call(u,this),this._listeners=g,null===(c=null===(a=this._options)||void 0===a?void 0:a.onDidAddFirstListener)||void 0===c||c.call(a,this)),this._size++;const L=(0,i.OF)((()=>{null==p||p.unregister(L),null==_||_(),this._removeListener(g)}));if(n instanceof i.SL?n.add(L):Array.isArray(n)&&n.push(L),p){const e=(new Error).stack.split("\n").slice(2).join("\n").trim();p.register(L,e,L)}return L}),this._event}_removeListener(e){var t,n,r,s;if(null===(n=null===(t=this._options)||void 0===t?void 0:t.onWillRemoveListener)||void 0===n||n.call(t,this),!this._listeners)return;if(1===this._size)return this._listeners=void 0,null===(s=null===(r=this._options)||void 0===r?void 0:r.onDidRemoveLastListener)||void 0===s||s.call(r,this),void(this._size=0);const i=this._listeners,o=i.indexOf(e);if(-1===o)throw new Error("Attempted to dispose unknown listener");this._size--,i[o]=void 0;const u=this._deliveryQueue.current===this;if(2*this._size<=i.length){let e=0;for(let t=0;t<i.length;t++)i[t]?i[e++]=i[t]:u&&(this._deliveryQueue.end--,e<this._deliveryQueue.i&&this._deliveryQueue.i--);i.length=e}}_deliver(e,t){var n;if(!e)return;const s=(null===(n=this._options)||void 0===n?void 0:n.onListenerError)||r.dL;if(s)try{e.value(t)}catch(e){s(e)}else e.value(t)}_deliverQueue(e){const t=e.current._listeners;for(;e.i<e.end;)this._deliver(t[e.i++],e.value);e.reset()}fire(e){var t,n,r,s;if((null===(t=this._deliveryQueue)||void 0===t?void 0:t.current)&&(this._deliverQueue(this._deliveryQueue),null===(n=this._perfMon)||void 0===n||n.stop()),null===(r=this._perfMon)||void 0===r||r.start(this._size),this._listeners)if(this._listeners instanceof v)this._deliver(this._listeners,e);else{const t=this._deliveryQueue;t.enqueue(this,e,this._listeners.length),this._deliverQueue(t)}else;null===(s=this._perfMon)||void 0===s||s.stop()}hasListeners(){return this._size>0}}const _=()=>new m;class m{constructor(){this.i=-1,this.end=0}enqueue(e,t,n){this.i=0,this.end=n,this.current=e,this.value=t}reset(){this.i=this.end,this.current=void 0,this.value=void 0}}class L extends g{constructor(e){super(e),this._isPaused=0,this._eventQueue=new o.S,this._mergeFn=null==e?void 0:e.merge}pause(){this._isPaused++}resume(){if(0!==this._isPaused&&0==--this._isPaused)if(this._mergeFn){if(this._eventQueue.size>0){const e=Array.from(this._eventQueue);this._eventQueue.clear(),super.fire(this._mergeFn(e))}}else for(;!this._isPaused&&0!==this._eventQueue.size;)super.fire(this._eventQueue.shift())}fire(e){this._size&&(0!==this._isPaused?this._eventQueue.push(e):super.fire(e))}}class w extends L{constructor(e){var t;super(e),this._delay=null!==(t=e.delay)&&void 0!==t?t:100}fire(e){this._handle||(this.pause(),this._handle=setTimeout((()=>{this._handle=void 0,this.resume()}),this._delay)),super.fire(e)}}class E extends g{constructor(e){super(e),this._queuedEvents=[],this._mergeFn=null==e?void 0:e.merge}fire(e){this.hasListeners()&&(this._queuedEvents.push(e),1===this._queuedEvents.length&&queueMicrotask((()=>{this._mergeFn?super.fire(this._mergeFn(this._queuedEvents)):this._queuedEvents.forEach((e=>super.fire(e))),this._queuedEvents=[]})))}}class C{constructor(){this.hasListeners=!1,this.events=[],this.emitter=new g({onWillAddFirstListener:()=>this.onFirstListenerAdd(),onDidRemoveLastListener:()=>this.onLastListenerRemove()})}get event(){return this.emitter.event}add(e){const t={event:e,listener:null};this.events.push(t),this.hasListeners&&this.hook(t);return(0,i.OF)((0,s.M)((()=>{this.hasListeners&&this.unhook(t);const e=this.events.indexOf(t);this.events.splice(e,1)})))}onFirstListenerAdd(){this.hasListeners=!0,this.events.forEach((e=>this.hook(e)))}onLastListenerRemove(){this.hasListeners=!1,this.events.forEach((e=>this.unhook(e)))}hook(e){e.listener=e.event((e=>this.emitter.fire(e)))}unhook(e){var t;null===(t=e.listener)||void 0===t||t.dispose(),e.listener=null}dispose(){var e;this.emitter.dispose();for(const t of this.events)null===(e=t.listener)||void 0===e||e.dispose();this.events=[]}}class k{constructor(){this.data=[]}wrapEvent(e,t,n){return(r,s,i)=>e((e=>{var i;const o=this.data[this.data.length-1];if(!t)return void(o?o.buffers.push((()=>r.call(s,e))):r.call(s,e));const u=o;u?(null!==(i=u.items)&&void 0!==i||(u.items=[]),u.items.push(e),0===u.buffers.length&&o.buffers.push((()=>{var e;null!==(e=u.reducedResult)&&void 0!==e||(u.reducedResult=n?u.items.reduce(t,n):u.items.reduce(t)),r.call(s,u.reducedResult)}))):r.call(s,t(n,e))}),void 0,i)}bufferEvents(e){const t={buffers:new Array};this.data.push(t);const n=e();return this.data.pop(),t.buffers.forEach((e=>e())),n}}class A{constructor(){this.listening=!1,this.inputEvent=l.None,this.inputEventListener=i.JT.None,this.emitter=new g({onDidAddFirstListener:()=>{this.listening=!0,this.inputEventListener=this.inputEvent(this.emitter.fire,this.emitter)},onDidRemoveLastListener:()=>{this.listening=!1,this.inputEventListener.dispose()}}),this.event=this.emitter.event}set input(e){this.inputEvent=e,this.listening&&(this.inputEventListener.dispose(),this.inputEventListener=e(this.emitter.fire,this.emitter))}dispose(){this.inputEventListener.dispose(),this.emitter.dispose()}}},15527:(e,t,n)=>{n.d(t,{KM:()=>c,ej:()=>u,fn:()=>l,oP:()=>d,yj:()=>a});var r=n(82663),s=n(1432),i=n(97295);function o(e){return 47===e||92===e}function u(e){return e.replace(/[\\/]/g,r.KR.sep)}function l(e){return-1===e.indexOf("/")&&(e=u(e)),/^[a-zA-Z]:(\/|$)/.test(e)&&(e="/"+e),e}function a(e,t=r.KR.sep){if(!e)return"";const n=e.length,s=e.charCodeAt(0);if(o(s)){if(o(e.charCodeAt(1))&&!o(e.charCodeAt(2))){let r=3;const s=r;for(;r<n&&!o(e.charCodeAt(r));r++);if(s!==r&&!o(e.charCodeAt(r+1)))for(r+=1;r<n;r++)if(o(e.charCodeAt(r)))return e.slice(0,r+1).replace(/[\\/]/g,t)}return t}if(h(s)&&58===e.charCodeAt(1))return o(e.charCodeAt(2))?e.slice(0,2)+t:e.slice(0,2);let i=e.indexOf("://");if(-1!==i)for(i+=3;i<n;i++)if(o(e.charCodeAt(i)))return e.slice(0,i+1);return""}function c(e,t,n,s=r.ir){if(e===t)return!0;if(!e||!t)return!1;if(t.length>e.length)return!1;if(n){if(!(0,i.ok)(e,t))return!1;if(t.length===e.length)return!0;let n=t.length;return t.charAt(t.length-1)===s&&n--,e.charAt(n)===s}return t.charAt(t.length-1)!==s&&(t+=s),0===e.indexOf(t)}function h(e){return e>=65&&e<=90||e>=97&&e<=122}function d(e,t=s.ED){return!!t&&(h(e.charCodeAt(0))&&58===e.charCodeAt(1))}},75392:(e,t,n)=>{n.d(t,{CL:()=>J,EW:()=>G,Ji:()=>u,KZ:()=>y,Oh:()=>P,Sy:()=>c,XU:()=>W,ir:()=>a,jB:()=>O,l7:()=>V,mB:()=>R,mX:()=>Z,or:()=>o});var r=n(43702),s=n(15490),i=n(97295);function o(...e){return function(t,n){for(let r=0,s=e.length;r<s;r++){const s=e[r](t,n);if(s)return s}return null}}l.bind(void 0,!1);const u=l.bind(void 0,!0);function l(e,t,n){if(!n||n.length<t.length)return null;let r;return r=e?i.ok(n,t):0===n.indexOf(t),r?t.length>0?[{start:0,end:t.length}]:[]:null}function a(e,t){const n=t.toLowerCase().indexOf(e.toLowerCase());return-1===n?null:[{start:n,end:n+e.length}]}function c(e,t){return h(e.toLowerCase(),t.toLowerCase(),0,0)}function h(e,t,n,r){if(n===e.length)return[];if(r===t.length)return null;if(e[n]===t[r]){let s=null;return(s=h(e,t,n+1,r+1))?C({start:r,end:r+1},s):null}return h(e,t,n,r+1)}function d(e){return 97<=e&&e<=122}function f(e){return 65<=e&&e<=90}function v(e){return 48<=e&&e<=57}function p(e){return 32===e||9===e||10===e||13===e}const g=new Set;function _(e){return p(e)||g.has(e)}function m(e,t){return e===t||_(e)&&_(t)}"()[]{}<>`'\"-/;:,.?!".split("").forEach((e=>g.add(e.charCodeAt(0))));const L=new Map;function w(e){if(L.has(e))return L.get(e);let t;const n=(0,s.C)(e);return n&&(t=n),L.set(e,t),t}function E(e){return d(e)||f(e)||v(e)}function C(e,t){return 0===t.length?t=[e]:e.end===t[0].start?t[0].start=e.start:t.unshift(e),t}function k(e,t){for(let n=t;n<e.length;n++){const t=e.charCodeAt(n);if(f(t)||v(t)||n>0&&!E(e.charCodeAt(n-1)))return n}return e.length}function A(e,t,n,r){if(n===e.length)return[];if(r===t.length)return null;if(e[n]!==t[r].toLowerCase())return null;{let s=null,i=r+1;for(s=A(e,t,n+1,r+1);!s&&(i=k(t,i))<t.length;)s=A(e,t,n+1,i),i++;return null===s?null:C({start:r,end:r+1},s)}}function b(e,t){if(!t)return null;if(0===(t=t.trim()).length)return null;if(!function(e){let t=0,n=0,r=0,s=0;for(let i=0;i<e.length;i++)r=e.charCodeAt(i),f(r)&&t++,d(r)&&n++,p(r)&&s++;return 0!==t&&0!==n||0!==s?t<=5:e.length<=30}(e))return null;t.length>60&&(t=t.substring(0,60));const n=function(e){let t=0,n=0,r=0,s=0,i=0;for(let o=0;o<e.length;o++)i=e.charCodeAt(o),f(i)&&t++,d(i)&&n++,E(i)&&r++,v(i)&&s++;return{upperPercent:t/e.length,lowerPercent:n/e.length,alphaPercent:r/e.length,numericPercent:s/e.length}}(t);if(!function(e){const{upperPercent:t,lowerPercent:n,alphaPercent:r,numericPercent:s}=e;return n>.2&&t<.8&&r>.6&&s<.2}(n)){if(!function(e){const{upperPercent:t,lowerPercent:n}=e;return 0===n&&t>.6}(n))return null;t=t.toLowerCase()}let r=null,s=0;for(e=e.toLowerCase();s<t.length&&null===(r=A(e,t,0,s));)s=k(t,s+1);return r}function y(e,t,n=!1){if(!t||0===t.length)return null;let r=null,s=0;for(e=e.toLowerCase(),t=t.toLowerCase();s<t.length&&(r=M(e,t,0,s,n),null===r);)s=x(t,s+1);return r}function M(e,t,n,r,s){let i=0;if(n===e.length)return[];if(r===t.length)return null;if(!m(e.charCodeAt(n),t.charCodeAt(r))){const s=w(e.charCodeAt(n));if(!s)return null;for(let e=0;e<s.length;e++)if(!m(s[e],t.charCodeAt(r+e)))return null;i+=s.length-1}let o=null,u=r+i+1;if(o=M(e,t,n+1,u,s),!s)for(;!o&&(u=x(t,u))<t.length;)o=M(e,t,n+1,u,s),u++;if(!o)return null;if(e.charCodeAt(n)!==t.charCodeAt(r)){const s=w(e.charCodeAt(n));if(!s)return o;for(let e=0;e<s.length;e++)if(s[e]!==t.charCodeAt(r+e))return o}return C({start:r,end:r+i+1},o)}function x(e,t){for(let n=t;n<e.length;n++)if(_(e.charCodeAt(n))||n>0&&_(e.charCodeAt(n-1)))return n;return e.length}const N=o(u,b,a),F=o(u,b,c),z=new r.z6(1e4);function P(e,t,n=!1){if("string"!=typeof e||"string"!=typeof t)return null;let r=z.get(e);r||(r=new RegExp(i.un(e),"i"),z.set(e,r));const s=r.exec(t);return s?[{start:s.index,end:s.index+s[0].length}]:n?F(e,t):N(e,t)}function W(e,t){const n=G(e,e.toLowerCase(),0,t,t.toLowerCase(),0,{firstMatchCanBeWeak:!0,boostFullMatch:!0});return n?R(n):null}function O(e,t,n,r,s,i){const o=Math.min(13,e.length);for(;n<o;n++){const o=G(e,t,n,r,s,i,{firstMatchCanBeWeak:!0,boostFullMatch:!0});if(o)return o}return[0,i]}function R(e){if(void 0===e)return[];const t=[],n=e[1];for(let r=e.length-1;r>1;r--){const s=e[r]+n,i=t[t.length-1];i&&i.end===s?i.end=s+1:t.push({start:s,end:s+1})}return t}const S=128;function T(){const e=[],t=[];for(let e=0;e<=S;e++)t[e]=0;for(let n=0;n<=S;n++)e.push(t.slice(0));return e}function Q(e){const t=[];for(let n=0;n<=e;n++)t[n]=0;return t}const D=Q(2*S),q=Q(2*S),$=T(),U=T(),I=T(),B=!1;function H(e,t){if(t<0||t>=e.length)return!1;const n=e.codePointAt(t);switch(n){case 95:case 45:case 46:case 32:case 47:case 92:case 39:case 34:case 58:case 36:case 60:case 62:case 40:case 41:case 91:case 93:case 123:case 125:return!0;case void 0:return!1;default:return!!i.C8(n)}}function j(e,t){if(t<0||t>=e.length)return!1;switch(e.charCodeAt(t)){case 32:case 9:return!0;default:return!1}}function K(e,t,n){return t[e]!==n[e]}var J;!function(e){e.Default=[-100,0],e.isDefault=function(e){return!e||2===e.length&&-100===e[0]&&0===e[1]}}(J||(J={}));class Z{constructor(e,t){this.firstMatchCanBeWeak=e,this.boostFullMatch=t}}function G(e,t,n,r,s,i,o=Z.default){const u=e.length>S?S:e.length,l=r.length>S?S:r.length;if(n>=u||i>=l||u-n>l-i)return;if(!function(e,t,n,r,s,i,o=!1){for(;t<n&&s<i;)e[t]===r[s]&&(o&&(D[t]=s),t+=1),s+=1;return t===n}(t,n,u,s,i,l,!0))return;!function(e,t,n,r,s,i){let o=e-1,u=t-1;for(;o>=n&&u>=r;)s[o]===i[u]&&(q[o]=u,o--),u--}(u,l,n,i,t,s);let a=1,c=1,h=n,d=i;const f=[!1];for(a=1,h=n;h<u;a++,h++){const o=D[h],v=q[h],p=h+1<u?q[h+1]:l;for(c=o-i+1,d=o;d<p;c++,d++){let u=Number.MIN_SAFE_INTEGER,p=!1;d<=v&&(u=X(e,t,h,n,r,s,d,l,i,0===$[a-1][c-1],f));let g=0;u!==Number.MAX_SAFE_INTEGER&&(p=!0,g=u+U[a-1][c-1]);const _=d>o,m=_?U[a][c-1]+($[a][c-1]>0?-5:0):0,L=d>o+1&&$[a][c-1]>0,w=L?U[a][c-2]+($[a][c-2]>0?-5:0):0;if(L&&(!_||w>=m)&&(!p||w>=g))U[a][c]=w,I[a][c]=3,$[a][c]=0;else if(_&&(!p||m>=g))U[a][c]=m,I[a][c]=2,$[a][c]=0;else{if(!p)throw new Error("not possible");U[a][c]=g,I[a][c]=1,$[a][c]=$[a-1][c-1]+1}}}if(B&&function(e,t,n,r){e=e.substr(t),n=n.substr(r)}(e,n,r,i),!f[0]&&!o.firstMatchCanBeWeak)return;a--,c--;const v=[U[a][c],i];let p=0,g=0;for(;a>=1;){let e=c;do{const t=I[a][e];if(3===t)e-=2;else{if(2!==t)break;e-=1}}while(e>=1);p>1&&t[n+a-1]===s[i+c-1]&&!K(e+i-1,r,s)&&p+1>$[a][e]&&(e=c),e===c?p++:p=1,g||(g=e),a--,c=e-1,v.push(c)}l-i===u&&o.boostFullMatch&&(v[0]+=2);const _=g-u;return v[0]-=_,v}function X(e,t,n,r,s,i,o,u,l,a,c){if(t[n]!==i[o])return Number.MIN_SAFE_INTEGER;let h=1,d=!1;return o===n-r?h=e[n]===s[o]?7:5:!K(o,s,i)||0!==o&&K(o-1,s,i)?!H(i,o)||0!==o&&H(i,o-1)?(H(i,o-1)||j(i,o-1))&&(h=5,d=!0):h=5:(h=e[n]===s[o]?7:5,d=!0),h>1&&n===r&&(c[0]=!0),d||(d=K(o,s,i)||H(i,o-1)||j(i,o-1)),n===r?o>l&&(h-=d?3:5):h+=a?d?2:0:d?0:1,o+1===u&&(h-=d?3:5),h}function V(e,t,n,r,s,i,o){return function(e,t,n,r,s,i,o,u){let l=G(e,t,n,r,s,i,u);if(l&&!o)return l;if(e.length>=3){const t=Math.min(7,e.length-1);for(let o=n+1;o<t;o++){const t=Y(e,o);if(t){const e=G(t,t.toLowerCase(),n,r,s,i,u);e&&(e[0]-=3,(!l||e[0]>l[0])&&(l=e))}}}return l}(e,t,n,r,s,i,!0,o)}function Y(e,t){if(t+1>=e.length)return;const n=e[t],r=e[t+1];return n!==r?e.slice(0,t)+r+n+e.slice(t+2):void 0}Z.default={boostFullMatch:!0,firstMatchCanBeWeak:!1}},88289:(e,t,n)=>{function r(e,t){const n=this;let r,s=!1;return function(){if(s)return r;if(s=!0,t)try{r=e.apply(n,arguments)}finally{t()}else r=e.apply(n,arguments);return r}}n.d(t,{M:()=>r})},53192:(e,t,n)=>{n.d(t,{AO:()=>v,Ic:()=>g,mt:()=>l});var r=n(75392),s=n(82663),i=n(1432),o=n(97295);const u=[void 0,[]];function l(e,t,n=0,r=0){const s=t;return s.values&&s.values.length>1?function(e,t,n,r){let s=0;const i=[];for(const o of t){const[t,l]=a(e,o,n,r);if("number"!=typeof t)return u;s+=t,i.push(...l)}return[s,c(i)]}(e,s.values,n,r):a(e,t,n,r)}function a(e,t,n,s){const i=(0,r.EW)(t.original,t.originalLowercase,n,e,e.toLowerCase(),s,{firstMatchCanBeWeak:!0,boostFullMatch:!0});return i?[i[0],(0,r.mB)(i)]:u}Object.freeze({score:0});function c(e){const t=e.sort(((e,t)=>e.start-t.start)),n=[];let r;for(const e of t)r&&h(r,e)?(r.start=Math.min(r.start,e.start),r.end=Math.max(r.end,e.end)):(r=e,n.push(e));return n}function h(e,t){return!(e.end<t.start)&&!(t.end<e.start)}function d(e){return e.startsWith('"')&&e.endsWith('"')}const f=" ";function v(e){"string"!=typeof e&&(e="");const t=e.toLowerCase(),{pathNormalized:n,normalized:r,normalizedLowercase:i}=p(e),o=n.indexOf(s.ir)>=0,u=d(e);let l;const a=e.split(f);if(a.length>1)for(const e of a){const t=d(e),{pathNormalized:n,normalized:r,normalizedLowercase:s}=p(e);r&&(l||(l=[]),l.push({original:e,originalLowercase:e.toLowerCase(),pathNormalized:n,normalized:r,normalizedLowercase:s,expectContiguousMatch:t}))}return{original:e,originalLowercase:t,pathNormalized:n,normalized:r,normalizedLowercase:i,values:l,containsPathSeparator:o,expectContiguousMatch:u}}function p(e){let t;t=i.ED?e.replace(/\//g,s.ir):e.replace(/\\/g,s.ir);const n=(0,o.R1)(t).replace(/\s|"/g,"");return{pathNormalized:t,normalized:n,normalizedLowercase:n.toLowerCase()}}function g(e){return Array.isArray(e)?v(e.map((e=>e.original)).join(f)):v(e.original)}}}]);