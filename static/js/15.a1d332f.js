(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[15],{"/h2V":function(t,e,n){"use strict";var a=n("jovR"),r=n.n(a);r.a},UExd:function(t,e,n){var a=n("DVgA"),r=n("aCFj"),o=n("UqcF").f;t.exports=function(t){return function(e){var n,i=r(e),l=a(i),s=l.length,c=0,u=[];while(s>c)o.call(i,n=l[c++])&&u.push(t?[n,i[n]]:i[n]);return u}}},Zcjg:function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("q-btn",{attrs:{icon:"search",color:"primary",glossy:"",label:"Поиск"},on:{click:function(e){t.showSearchDialog=!0}}},[t.showSearchDialog?n("q-modal",{attrs:{"content-css":"min-width: 30vw; max-height: 100%;","content-classes":"flex column justify-between"},on:{hide:t.clearForm},model:{value:t.showSearchDialog,callback:function(e){t.showSearchDialog=e},expression:"showSearchDialog"}},[n("q-toolbar",[n("q-toolbar-title",[t._v("\n\t\t\t\tПоиск документов\n\t\t\t")]),n("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{flat:"",icon:"close"}})],1),n("div",{staticClass:"q-px-sm"},[t.options.some(function(t){return"number"==t.type})?n("q-field",{attrs:{label:"Номер"}},[n("q-input",{attrs:{clearable:"",type:"number"},model:{value:t.form.number,callback:function(e){t.$set(t.form,"number",e)},expression:"form.number"}})],1):t._e(),t.options.some(function(t){return"date"==t.type})?n("q-field",{attrs:{label:"Дата"}},[n("q-datetime",{attrs:{clearable:"",type:"date",value:t.form.date,format:"DD.MM.YYYY"},on:{input:function(e){t.form.date=e?new Date(e).toLocaleDateString("EU"):null}}})],1):t._e(),t.options.some(function(t){return"month"==t.type})?n("q-field",{attrs:{label:"Период"}},[n("q-datetime",{attrs:{clearable:"",type:"date",value:t.form.month,format:"MM.YYYY",modal:"","default-view":"month"},on:{change:function(e){t.form.month=e?new Date(e).toLocaleDateString("EU"):null}}})],1):t._e(),t.options.some(function(t){return"station"==t.type})?n("q-field",{attrs:{label:"Участок"}},[n("q-select",{attrs:{options:t.stations.map(function(t){return{label:t.name,value:t.id}}),separator:"",clearable:""},model:{value:t.form.station,callback:function(e){t.$set(t.form,"station",e)},expression:"form.station"}})],1):t._e(),t.options.some(function(t){return"departament"==t.type})?n("q-field",{attrs:{label:"Отдел"}},[n("q-select",{attrs:{options:t.$store.state.main.departaments,clearable:"",separator:""},model:{value:t.form.departament,callback:function(e){t.$set(t.form,"departament",e)},expression:"form.departament"}})],1):t._e(),t.options.some(function(t){return"event"==t.type})?n("q-field",{attrs:{label:"Вид работ"}},[n("q-select",{attrs:{options:t.events.map(function(t){return{label:t.full_name,value:t.id}}),separator:"",clearable:""},model:{value:t.form.event,callback:function(e){t.$set(t.form,"event",e)},expression:"form.event"}})],1):t._e(),t.options.some(function(t){return"worker"==t.type})?n("q-field",{attrs:{label:"Работник"}},[n("q-select",{attrs:{options:t.workers.map(function(t){return{label:t.full_name,value:t.id}}),separator:"",clearable:""},model:{value:t.form.worker,callback:function(e){t.$set(t.form,"worker",e)},expression:"form.worker"}})],1):t._e(),t.options.some(function(t){return"car"==t.type})?n("q-field",{attrs:{label:"Автомобиль"}},[n("q-select",{attrs:{options:t.cars.map(function(t){return{label:t.full_name,value:t.id}}),separator:"",clearable:""},model:{value:t.form.car,callback:function(e){t.$set(t.form,"car",e)},expression:"form.car"}})],1):t._e()],1),n("q-toolbar",{staticClass:"justify-center group self-end"},[n("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{icon:"search",label:"Поиск",color:"positive",disabled:!t.is_valid},on:{click:t.searchDocument}}),n("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{icon:"close",label:"Отмена",color:"negative"}})],1)],1):t._e()],1)},r=[];a._withStripped=!0;n("dRSK"),n("RW0V"),n("OG14"),n("f3/d"),n("rGqo"),n("yt8O"),n("hhXQ");var o={name:"SearchingPanel",props:{search:{required:!0,type:Function},options:{type:Array,required:!0}},data:function(){return{form:{number:null,car:null,station:null,event:null,worker:null,departament:null,date:null,month:null},stations:[],events:[],workers:[],cars:[],showSearchDialog:!1,field:null,value:null,fetched_data:[]}},computed:{is_valid:function(){return Object.values(this.form).some(function(t){return null!=t&&""!=t})}},methods:{searchDocument:function(){var t=this;if(this.is_valid){var e={};this.options.forEach(function(n){null!=t.form[n.type]&&""!=t.form[n.type]&&("month"==n.type?e[n.name]=new Date(t.form[n.type]).getMonth()+1:e[n.name]=t.form[n.type])}),this.search(e)}},getStations:function(){var t=this;this.$axios.get("/api/v1/stations/").then(function(e){t.stations=e.data.stations}).catch(function(e){t.handleError(e)})},getCars:function(){var t=this;this.$axios.get("/api/v1/car/").then(function(e){t.cars=e.data.cars}).catch(function(e){t.handleError(e)})},getWorkers:function(){var t=this;this.$axios.get("/api/v1/workers/").then(function(e){t.workers=e.data.workers}).catch(function(e){t.handleError(e)})},getEvents:function(){var t=this;this.$axios.get("/api/v1/outfit_events/").then(function(e){t.events=e.data.outfit_events}).catch(function(e){t.handleError(e)})},handleError:function(t){this.$q.notify({message:t.message,icon:"error",position:"bottom-right"})},clearForm:function(){var t=this;Object.keys(this.form).forEach(function(e){return t.form[e]=null})}},mounted:function(){this.options.find(function(t){return"station"==t.type})&&this.getStations(),this.options.find(function(t){return"worker"==t.type})&&this.getWorkers(),this.options.find(function(t){return"car"==t.type})&&this.getCars(),this.options.find(function(t){return"event"==t.type})&&this.getEvents()}},i=o,l=(n("/h2V"),n("KHd+")),s=Object(l["a"])(i,a,r,!1,null,null,null);e["a"]=s.exports},ZqoW:function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("div",{staticClass:"row justify-between group"},[n("div",{staticClass:"col-auto group"},[n("q-btn",{attrs:{icon:"add",color:"positive",type:"button",glossy:"",label:"Создать"},nativeOn:{click:function(e){t.$router.push({name:"NewTractorRegForm"})}}}),n("searching-panel",{attrs:{options:t.options,search:t.getRegForms}})],1)]),n("q-table",{attrs:{data:t.regforms,columns:t.columns,"row-key":"id",dense:!t.$q.platform.is.desktop,loading:t.loading,"rows-per-page-options":[20,50,100],separator:"cell",pagination:t.pagination,"hide-bottom":""},scopedSlots:t._u([{key:"body-cell-options",fn:function(e){return n("q-td",{attrs:{props:e}},[n("q-btn",{attrs:{icon:"print",dense:"",flat:"",color:"primary"},nativeOn:{click:function(n){t.$router.push({name:"PrintRegForm",params:{id:e.row.id}})}}})],1)}}])})],1)},r=[];a._withStripped=!0;n("f3/d");var o=n("Zcjg"),i={name:"TractorRegFormListPage",components:{"searching-panel":o["a"]},data:function(){return{loading:!1,pagination:{rowsPerPage:20},regforms:[],options:[{name:"id",type:"number"},{name:"date",type:"date"},{name:"brigadier",type:"worker"},{name:"driver",type:"worker"},{name:"station",type:"station"},{name:"car",type:"car"}],columns:[{name:"options",label:"Опции",field:"id",align:"center"},{name:"number",label:"Номер",field:"id",align:"center"},{name:"date",label:"Дата",field:function(t){return new Date(t.date).toLocaleDateString()},align:"center"},{name:"brigadier",label:"Бригадир",field:function(t){return t.brigadier.full_name},align:"center"},{name:"driver",label:"Тракторист",field:function(t){return t.driver.full_name},align:"center"},{name:"station",label:"Участок",field:function(t){return t.station.name},align:"center"},{name:"departament",label:"Отдел",field:function(t){return t.departament_full},align:"center"},{name:"car",label:"Трактор",field:function(t){return t.car.full_name},align:"center"}]}},methods:{getRegForms:function(t){var e=this;this.loading=!0,this.$axios.get("/api/v1/tractor-regform/",{params:t}).then(function(t){e.regforms=t.data.regforms}).catch(function(t){}).finally(function(){e.loading=!1})}}},l=i,s=n("KHd+"),c=Object(s["a"])(l,a,r,!1,null,null,null);e["default"]=c.exports},hhXQ:function(t,e,n){var a=n("XKFU"),r=n("UExd")(!1);a(a.S,"Object",{values:function(t){return r(t)}})},jovR:function(t,e,n){}}]);