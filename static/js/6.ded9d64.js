(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[6],{RhWv:function(t,s,e){"use strict";e.r(s);var a=function(){var t=this,s=t.$createElement,e=t._self._c||s;return e("div",[e("q-toolbar",{staticClass:"group",attrs:{color:"indigo"}},[e("q-btn",{attrs:{icon:"add",label:"Новое",color:"positive",glossy:""},nativeOn:{click:function(s){t.$store.commit("main/showNewMessage",!0)}}})],1),e("q-list",{staticClass:"no-padding",attrs:{link:"",dense:"",multiline:"",separator:""}},t._l(t.chats,function(s){return e("q-item",{key:s.id,staticStyle:{padding:"5px"},attrs:{to:{name:"ViewChat",params:{id:s.id}}}},[e("q-item-side",{staticClass:"col-xs-3 col-md-2",attrs:{align:"center"}},[e("q-item-tile",{attrs:{avatar:""}},[e("img",{attrs:{src:s.members.filter(function(s){return s.id!=t.$user.id})[0].avatar||"statics/anon.png"}})]),e("q-item-tile",{attrs:{stamp:"",color:"dark"}},[t._v(t._s(s.members.filter(function(s){return s.id!=t.$user.id})[0].full_name))]),e("q-item-tile",{attrs:{stamp:""}},[t._v(t._s(t.parseDate(s.messages[0].created_date)[0]))]),e("q-item-tile",{attrs:{stamp:""}},[t._v(t._s(t.parseDate(s.messages[0].created_date)[1]))])],1),e("q-item-main",{class:s.messages[0].is_new?"bg-green-2":""},[s.messages[0].sender.id==t.$user.id?e("q-item-tile",{attrs:{stamp:""}},[e("img",{staticClass:"avatar",staticStyle:{width:"25px",height:"25px"},attrs:{src:s.messages[0].sender.avatar||"statics/anon.png"}}),e("span",[t._v(t._s(s.messages[0].sender.full_name))])]):e("q-item-tile",{staticClass:"q-pa-xs",attrs:{label:""}},[t._v(t._s(t.truncate(s.messages[0].title,19)))]),e("q-item-tile",{staticClass:"shadow-1 round-orders q-pa-xs",attrs:{sublabel:""}},[t._v(t._s(t.truncate(s.messages[0].text,25)))]),s.messages[0].files.length?e("q-item-tile",{attrs:{icon:"attachment",color:"primary"}},[e("q-tooltip",{attrs:{color:"red"}},[t._v("Прикрепленные файлы: "+t._s(s.messages[0].files.map(function(t){return t.title})))])],1):t._e()],1)],1)}))],1)},i=[];a._withStripped=!0;var n={name:"IncomingMessagesPage",data:function(){return{chats:[]}},methods:{getChats:function(){var t=this,s={member:this.$user.id};this.$axios.get("/api/v1/chats/",{params:s}).then(function(s){t.chats=s.data.chats}).catch(function(s){t.$q.notify({message:s.message})})},parseDate:function(t){var s=new Date(t);return[s.toLocaleDateString(),s.toLocaleTimeString()]},truncate:function(t,s){return this.$store.state.main.screen.width>360&&(s*=5),t.length>s?t.slice(0,s-3)+"...":t}},mounted:function(){this.getChats()}},r=n,c=(e("znsL"),e("KHd+")),l=Object(c["a"])(r,a,i,!1,null,null,null);s["default"]=l.exports},bBqO:function(t,s,e){},znsL:function(t,s,e){"use strict";var a=e("bBqO"),i=e.n(a);i.a}}]);