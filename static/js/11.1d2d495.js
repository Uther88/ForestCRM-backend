(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[11],{"YVt+":function(e,t,s){"use strict";var r=s("hTN+"),i=s.n(r);i.a},"ZXG/":function(e,t,s){"use strict";s.r(t);var r=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("q-page",[s("q-list",{attrs:{separator:"",link:""}},[e.$store.state.main.user.is_staff?s("q-list-header",[s("q-btn",{attrs:{icon:"add",color:"positive",glossy:"",label:"Новый"},nativeOn:{click:function(t){e.showNewUser=!e.showNewUser}}})],1):e._e(),e._l(e.$store.state.main.users,function(t){return s("q-item",{key:t.id,staticClass:"cursor-pointer"},[s("q-item-side",{nativeOn:{click:function(s){e.viewUser(t)}}},[s("q-item-tile",{attrs:{avatar:""}},[s("img",{attrs:{src:t.avatar||"statics/anon.png"}})])],1),s("q-item-main",{nativeOn:{click:function(s){e.viewUser(t)}}},[s("q-item-tile",[e._v(e._s(t.last_name)+" "+e._s(t.first_name)+" "+e._s(t.third_name))]),s("q-item-tile",{attrs:{sublabel:""}},[e._v(e._s(t.position))])],1),s("q-item-side",{staticClass:"group"},[t.id==e.$store.state.main.user.id?s("q-btn",{attrs:{icon:"edit",color:"primary",round:""},nativeOn:{click:function(s){e.editUser(t)}}}):s("q-btn",{attrs:{icon:"message",round:"",color:"deep-orange"},nativeOn:{click:function(s){e.$store.dispatch("main/showNewMessage",t.id)}}}),t.id!=e.$store.state.main.user.id?s("q-btn",{attrs:{icon:"event_note",round:"",color:"green"},nativeOn:{click:function(s){e.$router.push({name:"newTask",params:{user:t.id}})}}}):e._e()],1)],1)}),e.selectedUser?s("q-modal",{ref:"userDetail",attrs:{"content-css":"max-height:100%;"},model:{value:e.showDetail,callback:function(t){e.showDetail=t},expression:"showDetail"}},[s("div",{staticClass:"flex column full-height justify-between bg-grey-4",staticStyle:{"min-width":"30vw"}},[s("q-toolbar",{attrs:{glossy:""}},[s("q-toolbar-title",{staticClass:"text-center"},[e._v("Профиль сотрудника")])],1),s("div",{staticClass:"flex row justify-center"},[s("div",{staticClass:"text-center q-pt-sm"},[s("img",{staticClass:"shadow-3",staticStyle:{width:"100%","max-width":"220px",height:"auto","border-radius":"8px"},attrs:{src:e.selectedUser.avatar||"statics/anon.png"}})]),s("div",{staticClass:"shadow-1 q-pa-xs fit bg-white round-borders q-ma-sm"},[s("table",{staticClass:"q-table user-info"},[s("tr",[s("td",[e._v("\n                  Фамилия\n                  ")]),s("td",[e._v("\n                    "+e._s(e.selectedUser.last_name)+"\n                  ")])]),s("tr",[s("td",[e._v("\n                    Имя\n                  ")]),s("td",[e._v("\n                    "+e._s(e.selectedUser.first_name)+"\n                  ")])]),s("tr",[s("td",[e._v("\n                  Отчество\n                  ")]),s("td",[e._v("\n                    "+e._s(e.selectedUser.third_name)+"\n                  ")])]),s("tr",[s("td",[e._v("\n                  Должность\n                  ")]),s("td",[e._v("\n                    "+e._s(e.selectedUser.position)+"\n                  ")])]),s("tr",[s("td",[e._v("\n                  Email\n                  ")]),s("td",[e._v("\n                    "+e._s(e.selectedUser.email||"Нет")+"\n                  ")])])])])]),s("q-toolbar",{staticClass:"justify-end",attrs:{glossy:""}},[s("q-btn",{attrs:{label:"Закрыть",icon:"close",color:"positive"},nativeOn:{click:function(t){e.showDetail=!e.showDetail}}})],1)],1)]):e._e(),s("q-modal",{on:{hide:e.resetForm},model:{value:e.showNewUser,callback:function(t){e.showNewUser=t},expression:"showNewUser"}},[s("div",{staticClass:"flex column full-height  justify-between",staticStyle:{"min-width":"30vw"}},[s("q-toolbar",{attrs:{color:"primary"}},[s("q-toolbar-title",[e._v("Новый сотрудник")]),s("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{icon:"close",flat:""}})],1),s("div",{staticClass:"flex column q-pa-sm"},[s("q-field",{attrs:{label:"Логин:",icon:"person","icon-color":e.userForm.username?"positive":"faded"}},[s("q-input",{attrs:{type:"text"},model:{value:e.userForm.username,callback:function(t){e.$set(e.userForm,"username","string"===typeof t?t.trim():t)},expression:"userForm.username"}})],1),s("q-field",{attrs:{label:"Пароль:",icon:"lock","icon-color":e.userForm.password?"positive":"faded"}},[s("q-input",{attrs:{type:"password"},model:{value:e.userForm.password,callback:function(t){e.$set(e.userForm,"password","string"===typeof t?t.trim():t)},expression:"userForm.password"}})],1),s("q-field",{attrs:{label:"Фамилия:",icon:"assignment","icon-color":e.userForm.last_name?"positive":"faded"}},[s("q-input",{attrs:{type:"text"},model:{value:e.userForm.last_name,callback:function(t){e.$set(e.userForm,"last_name","string"===typeof t?t.trim():t)},expression:"userForm.last_name"}})],1),s("q-field",{attrs:{label:"Имя:",icon:"assignment","icon-color":e.userForm.first_name?"positive":"faded"}},[s("q-input",{attrs:{type:"text"},model:{value:e.userForm.first_name,callback:function(t){e.$set(e.userForm,"first_name","string"===typeof t?t.trim():t)},expression:"userForm.first_name"}})],1),s("q-field",{attrs:{label:"Отчество:",icon:"assignment","icon-color":e.userForm.third_name?"positive":"faded"}},[s("q-input",{attrs:{type:"text"},model:{value:e.userForm.third_name,callback:function(t){e.$set(e.userForm,"third_name","string"===typeof t?t.trim():t)},expression:"userForm.third_name"}})],1),s("q-field",{attrs:{label:"@mail:",icon:"email","icon-color":e.validateEmail()?"positive":"faded"}},[s("q-input",{attrs:{type:"email"},model:{value:e.userForm.email,callback:function(t){e.$set(e.userForm,"email","string"===typeof t?t.trim():t)},expression:"userForm.email"}})],1),s("q-field",{attrs:{label:"Должность:",icon:"assignment_ind","icon-color":e.userForm.position?"positive":"faded"}},[s("q-input",{attrs:{type:"text"},model:{value:e.userForm.position,callback:function(t){e.$set(e.userForm,"position","string"===typeof t?t.trim():t)},expression:"userForm.position"}})],1),s("q-field",{attrs:{label:"Аватар:",icon:"image","icon-color":e.userForm.avatar?"positive":"faded"}},[s("q-uploader",{ref:"fileField",attrs:{url:"","hide-upload-button":!0,"hide-underline":"",extensions:".gif,.jpg,.jpeg,.png","auto-expand":""},on:{add:function(t){e.userForm.avatar=t[0]},"remove:cancel":function(t){e.userForm.avatar=null}}})],1)],1),s("q-toolbar",{staticClass:"justify-around self-end"},[s("q-btn",{attrs:{icon:"save",color:"positive",label:"Сохранить",disabled:!e.is_valid},nativeOn:{click:function(t){return e.saveUser(t)}}}),s("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{icon:"close",color:"negative",label:"Отмена"}})],1)],1)])],2)],1)},i=[];r._withStripped=!0;s("yt8O"),s("RW0V"),s("rGqo");var a={name:"UsersPage",data:function(){return{showDetail:!1,showNewUser:!1,selectedUser:null,editableUser:null,userForm:{username:"",password:"",first_name:"",last_name:"",third_name:"",position:"",email:"",avatar:""}}},methods:{resetForm:function(){var e=this;Object.keys(this.userForm).forEach(function(t){return e.userForm[t]=""})},validateEmail:function(){var e=/\S+@\S+\.\S+/;return e.test(this.userForm.email)},viewUser:function(e){this.selectedUser=e,this.showDetail=!0},editUser:function(e){var t=this;this.editableUser=e,Object.keys(this.userForm).forEach(function(s){return t.userForm[s]=e[s]||""}),this.showNewUser=!0},saveUser:function(){var e=this;if(this.is_valid){var t=new FormData;Object.keys(this.userForm).forEach(function(s){return t.set(s,e.userForm[s])}),this.$axios({method:this.editableUser?"PUT":"POST",url:"/api/v1/users/",params:this.editableUser?{pk:this.editableUser.id}:{},data:t}).then(function(t){e.showNewUser=!1,e.editableUser.id==e.$store.state.main.user.id?e.$root.logout():e.$root.getUsers()}).catch(function(t){e.$root.handleError(t.message)})}}},computed:{is_valid:function(){var e=this;return!(this.userForm.email&&!this.validateEmail())&&(!!Object.keys(this.userForm).filter(function(e){return"avatar"!=e&&"email"!=e}).every(function(t){return""!=e.userForm[t]})||void 0)}}},o=a,n=(s("YVt+"),s("KHd+")),l=Object(n["a"])(o,r,i,!1,null,null,null);t["default"]=l.exports},"hTN+":function(e,t,s){}}]);