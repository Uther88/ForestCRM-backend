(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[13],{"/h2V":function(t,e,n){"use strict";var a=n("jovR"),o=n.n(a);o.a},"8f8f":function(t,e,n){"use strict";var a=n("z4Yy"),o=n.n(a);o.a},UExd:function(t,e,n){var a=n("DVgA"),o=n("aCFj"),r=n("UqcF").f;t.exports=function(t){return function(e){var n,i=o(e),s=a(i),l=s.length,c=0,u=[];while(l>c)r.call(i,n=s[c++])&&u.push(t?[n,i[n]]:i[n]);return u}}},Zcjg:function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("q-btn",{attrs:{icon:"search",color:"primary",glossy:"",label:"Поиск"},on:{click:function(e){t.showSearchDialog=!0}}},[t.showSearchDialog?n("q-modal",{attrs:{"content-css":"min-width: 30vw; max-height: 100%;","content-classes":"flex column justify-between"},on:{hide:t.clearForm},model:{value:t.showSearchDialog,callback:function(e){t.showSearchDialog=e},expression:"showSearchDialog"}},[n("q-toolbar",[n("q-toolbar-title",[t._v("\n\t\t\t\tПоиск документов\n\t\t\t")]),n("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{flat:"",icon:"close"}})],1),n("div",{staticClass:"q-px-sm"},[t.options.some(function(t){return"number"==t.type})?n("q-field",{attrs:{label:"Номер"}},[n("q-input",{attrs:{clearable:"",type:"number"},model:{value:t.form.number,callback:function(e){t.$set(t.form,"number",e)},expression:"form.number"}})],1):t._e(),t.options.some(function(t){return"date"==t.type})?n("q-field",{attrs:{label:"Дата"}},[n("q-datetime",{attrs:{clearable:"",type:"date",value:t.form.date,format:"DD.MM.YYYY"},on:{input:function(e){t.form.date=e?new Date(e).toLocaleDateString("EU"):null}}})],1):t._e(),t.options.some(function(t){return"month"==t.type})?n("q-field",{attrs:{label:"Период"}},[n("q-datetime",{attrs:{clearable:"",type:"date",value:t.form.month,format:"MM.YYYY",modal:"","default-view":"month"},on:{change:function(e){t.form.month=e?new Date(e).toLocaleDateString("EU"):null}}})],1):t._e(),t.options.some(function(t){return"station"==t.type})?n("q-field",{attrs:{label:"Участок"}},[n("q-select",{attrs:{options:t.stations.map(function(t){return{label:t.name,value:t.id}}),separator:"",clearable:""},model:{value:t.form.station,callback:function(e){t.$set(t.form,"station",e)},expression:"form.station"}})],1):t._e(),t.options.some(function(t){return"departament"==t.type})?n("q-field",{attrs:{label:"Отдел"}},[n("q-select",{attrs:{options:t.$store.state.main.departaments,clearable:"",separator:""},model:{value:t.form.departament,callback:function(e){t.$set(t.form,"departament",e)},expression:"form.departament"}})],1):t._e(),t.options.some(function(t){return"event"==t.type})?n("q-field",{attrs:{label:"Вид работ"}},[n("q-select",{attrs:{options:t.events.map(function(t){return{label:t.full_name,value:t.id}}),separator:"",clearable:""},model:{value:t.form.event,callback:function(e){t.$set(t.form,"event",e)},expression:"form.event"}})],1):t._e(),t.options.some(function(t){return"worker"==t.type})?n("q-field",{attrs:{label:"Работник"}},[n("q-select",{attrs:{options:t.workers.map(function(t){return{label:t.full_name,value:t.id}}),separator:"",clearable:""},model:{value:t.form.worker,callback:function(e){t.$set(t.form,"worker",e)},expression:"form.worker"}})],1):t._e(),t.options.some(function(t){return"car"==t.type})?n("q-field",{attrs:{label:"Автомобиль"}},[n("q-select",{attrs:{options:t.cars.map(function(t){return{label:t.full_name,value:t.id}}),separator:"",clearable:""},model:{value:t.form.car,callback:function(e){t.$set(t.form,"car",e)},expression:"form.car"}})],1):t._e()],1),n("q-toolbar",{staticClass:"justify-center group self-end"},[n("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{icon:"search",label:"Поиск",color:"positive",disabled:!t.is_valid},on:{click:t.searchDocument}}),n("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{icon:"close",label:"Отмена",color:"negative"}})],1)],1):t._e()],1)},o=[];a._withStripped=!0;n("dRSK"),n("RW0V"),n("OG14"),n("f3/d"),n("rGqo"),n("yt8O"),n("hhXQ");var r={name:"SearchingPanel",props:{search:{required:!0,type:Function},options:{type:Array,required:!0}},data:function(){return{form:{number:null,car:null,station:null,event:null,worker:null,departament:null,date:null,month:null},stations:[],events:[],workers:[],cars:[],showSearchDialog:!1,field:null,value:null,fetched_data:[]}},computed:{is_valid:function(){return Object.values(this.form).some(function(t){return null!=t&&""!=t})}},methods:{searchDocument:function(){var t=this;if(this.is_valid){var e={};this.options.forEach(function(n){null!=t.form[n.type]&&""!=t.form[n.type]&&("month"==n.type?e[n.name]=new Date(t.form[n.type]).getMonth()+1:e[n.name]=t.form[n.type])}),this.search(e)}},getStations:function(){var t=this;this.$axios.get("/api/v1/stations/").then(function(e){t.stations=e.data.stations}).catch(function(e){t.handleError(e)})},getCars:function(){var t=this;this.$axios.get("/api/v1/car/").then(function(e){t.cars=e.data.cars}).catch(function(e){t.handleError(e)})},getWorkers:function(){var t=this;this.$axios.get("/api/v1/workers/").then(function(e){t.workers=e.data.workers}).catch(function(e){t.handleError(e)})},getEvents:function(){var t=this;this.$axios.get("/api/v1/outfit_events/").then(function(e){t.events=e.data.outfit_events}).catch(function(e){t.handleError(e)})},handleError:function(t){this.$q.notify({message:t.message,icon:"error",position:"bottom-right"})},clearForm:function(){var t=this;Object.keys(this.form).forEach(function(e){return t.form[e]=null})}},mounted:function(){this.options.find(function(t){return"station"==t.type})&&this.getStations(),this.options.find(function(t){return"worker"==t.type})&&this.getWorkers(),this.options.find(function(t){return"car"==t.type})&&this.getCars(),this.options.find(function(t){return"event"==t.type})&&this.getEvents()}},i=r,s=(n("/h2V"),n("KHd+")),l=Object(s["a"])(i,a,o,!1,null,null,null);e["a"]=l.exports},cI9m:function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("q-page",{staticClass:"fit"},[n("div",{staticClass:"row justify-between group"},[n("div",{staticClass:"col-auto group"},[n("q-btn",{attrs:{icon:"add",color:"positive",type:"button",glossy:"",label:"Создать"},nativeOn:{click:function(e){t.$router.push({name:"OutfitNew"})}}}),n("searching-panel",{attrs:{options:t.options,search:t.getDocuments}})],1)]),n("q-table",{attrs:{"table-style":"min-height: calc(100vh - 233px);","table-class":"outfitsTable",data:t.outfits,columns:t.columns,"row-key":"id",dense:!t.$q.platform.is.desktop,loading:t.loading,pagination:{rowsPerPage:0}},scopedSlots:t._u([{key:"body-cell-options",fn:function(e){return n("q-td",{attrs:{props:e}},[n("q-btn",{attrs:{icon:"print",color:"primary"},nativeOn:{click:function(n){t.$router.push({name:"outfitsPrint",params:{id:e.row.id}})}}})],1)}}])})],1)},o=[];a._withStripped=!0;n("rGqo"),n("f3/d");var r=n("Zcjg"),i={name:"OutfitsList",components:{"searching-panel":r["a"]},data:function(){return{loading:!1,outfits:[],options:[{name:"station",type:"station"},{name:"event",type:"event"},{name:"departament",type:"departament"},{name:"begin__month",type:"month"}],columns:[{name:"options",label:"Опции",field:"id",align:"center"},{name:"number",label:"Номер",field:"id",align:"center"},{name:"begin",label:"Начало",field:function(t){return new Date(t.begin).toLocaleDateString()},align:"center"},{name:"end",label:"Конец",field:function(t){return new Date(t.end).toLocaleDateString()},align:"center"},{name:"station",label:"Участок",field:function(t){return t.station.name},align:"center"},{name:"departament",label:"Отдел",field:"departament_full",align:"center"},{name:"forestry",label:"Лесничество",field:"forestry",align:"center"},{name:"event",label:"Мероприятие",field:function(t){return t.event.full_name},align:"center"},{name:"brigadier",label:"Бригадир",field:function(t){return t.brigadier.full_name},align:"center"}]}},methods:{getDocuments:function(t){var e=this,n={};this.options.forEach(function(e){n[e.name]=t[e.name]}),this.$axios.get("/api/v1/outfit/",{params:n}).then(function(t){e.outfits=t.data.outfits}).catch(function(t){})}}},s=i,l=(n("8f8f"),n("KHd+")),c=Object(l["a"])(s,a,o,!1,null,null,null);e["default"]=c.exports},hhXQ:function(t,e,n){var a=n("XKFU"),o=n("UExd")(!1);a(a.S,"Object",{values:function(t){return o(t)}})},jovR:function(t,e,n){},z4Yy:function(t,e,n){}}]);