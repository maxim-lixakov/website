(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{18:function(e,t,n){},19:function(e,t,n){},25:function(e,t,n){"use strict";n.r(t);var a=n(0),c=n.n(a),i=n(6),s=n.n(i),r=(n(18),n.p,n(19),n(2)),o=(n(21),n(22),n(9)),l=n(10),j=n(5),d=n(12),u=n(11),h=n(4),b=[],O=function(e){Object(d.a)(n,e);var t=Object(u.a)(n);function n(e){var a;return Object(o.a)(this,n),(a=t.call(this,e)).state={value:"coconut"},a.handleChange=a.handleChange.bind(Object(j.a)(a)),a.handleSubmit=a.handleSubmit.bind(Object(j.a)(a)),a}return Object(l.a)(n,[{key:"handleChange",value:function(e){x(e.target.value),this.setState({value:e.target.value})}},{key:"handleSubmit",value:function(e){e.preventDefault()}},{key:"render",value:function(){return Object(r.jsx)("form",{onSubmit:this.handleSubmit,children:Object(r.jsxs)("label",{children:["\u041a\u0438\u043b\u043e\u043c\u0435\u0442\u0440\u0430\u0436 \u043f\u043e :",Object(r.jsxs)("select",{value:this.state.value,onChange:this.handleChange,id:"select",children:[Object(r.jsx)("option",{value:"months",children:"\u043c\u0435\u0441\u044f\u0446\u0430\u043c"}),Object(r.jsx)("option",{value:"days",children:"\u0434\u043d\u044f\u043c"}),Object(r.jsx)("option",{value:"weeks",children:"\u043d\u0435\u0434\u0435\u043b\u044f\u043c"})]})]})})}}]),n}(c.a.Component),v=[{name:"\u043c\u0435\u0441\u044f\u0446",data:[400,358,418,425],color:"#D97706"}],x=function(e){if("days"===e){e=[];var t=new XMLHttpRequest;t.open("GET","http://127.0.0.1:8000/main/getData/",!1),t.setRequestHeader("Access-Control-Allow-Headers","*"),t.send();var n="";t.addEventListener("load",(function(){200===t.status&&(n=t.responseText)})),n=parseInt(n);for(var a=1;a<=n;a++)e.push(a)}},p=b.map((function(e){return e*e}));v[0].data=p;var f=function(e){return Object(r.jsxs)(h.a,{pannable:!0,zoomable:!0,style:{height:350},children:[Object(r.jsx)(h.g,{text:"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u043a\u0430"}),Object(r.jsx)(h.d,{position:"top",orientation:"horizontal"}),Object(r.jsx)(h.h,{children:Object(r.jsx)(h.i,{title:{text:"\u043a\u0438\u043b\u043e\u043c\u0435\u0442\u0440\u044b"},min:0,max:500})}),Object(r.jsx)(h.b,{children:Object(r.jsx)(h.c,{categories:b})}),Object(r.jsx)(h.e,{children:v.map((function(e,t){return Object(r.jsx)(h.f,{type:"line",tooltip:{visible:!0},data:e.data,name:e.name},t)}))})]})};var m=function(){return Object(r.jsx)("div",{className:"App",children:Object(r.jsx)("div",{className:"container",children:Object(r.jsxs)("div",{className:"section",children:[Object(r.jsx)("div",{className:"react-form",children:Object(r.jsx)(O,{})}),Object(r.jsx)(f,{})]})})})},g=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,26)).then((function(t){var n=t.getCLS,a=t.getFID,c=t.getFCP,i=t.getLCP,s=t.getTTFB;n(e),a(e),c(e),i(e),s(e)}))};s.a.render(Object(r.jsx)(c.a.StrictMode,{children:Object(r.jsx)(m,{})}),document.getElementById("root")),g()}},[[25,1,2]]]);
//# sourceMappingURL=main.82957b86.chunk.js.map