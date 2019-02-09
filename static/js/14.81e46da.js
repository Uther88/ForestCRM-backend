(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[14],{"61sT":function(t,e,o){"use strict";o.r(e);var a=function(){var t=this,e=this,o=e.$createElement,a=e._self._c||o;return a("q-stepper",{ref:"stepper",staticClass:"outfit",attrs:{color:"positive",contractable:"","alternative-labels":""},model:{value:e.currentSection,callback:function(t){e.currentSection=t},expression:"currentSection"}},[a("q-step",{attrs:{name:"main",title:"Главное",subtitle:"Основные данные",order:1,"active-icon":"assignment",icon:"assignment"}},[a("div",{staticClass:"row outfit-form flex-center group q-py-md full-height"},[a("div",{staticClass:"col-md-5 col-xs-12 q-pa-md shadow-1 full-height"},[a("q-field",{attrs:{label:"Участок:",icon:"location_city","icon-color":e.form.station?"positive":"negative",orientation:"horizontal"}},[a("q-select",{attrs:{options:e.options.stations.map(function(t){return{label:t.name,value:t.id}}),separator:"",placeholder:"Выберите участок"},model:{value:e.form.station,callback:function(t){e.$set(e.form,"station",t)},expression:"form.station"}})],1),a("q-field",{attrs:{label:"Отдел:",icon:"stars","icon-color":e.form.departament?"positive":"negative",orientation:"horizontal"}},[a("q-select",{attrs:{options:e.options.departaments,separator:"",placeholder:"Выберите отдел"},model:{value:e.form.departament,callback:function(t){e.$set(e.form,"departament",t)},expression:"form.departament"}})],1),a("q-field",{attrs:{label:"Лесничество:",icon:"panorama","icon-color":e.form.forestry?"positive":"negative",orientation:"horizontal"}},[a("q-input",{attrs:{type:"text",autocomplete:"on",placeholder:"Укажите лесничество"},model:{value:e.form.forestry,callback:function(t){e.$set(e.form,"forestry",t)},expression:"form.forestry"}})],1),a("q-field",{attrs:{label:"Мероприятие:",icon:"gavel","icon-color":e.form.event?"positive":"negative",orientation:"horizontal"}},[a("q-select",{attrs:{options:e.options.outfit_events.map(function(t){return{label:t.full_name,value:t.id}}),filter:"",placeholder:"Выберите мероприятие","filter-placeholder":"Поиск",separator:"","autofocus-filter":!1},model:{value:e.form.event,callback:function(t){e.$set(e.form,"event",t)},expression:"form.event"}})],1),a("q-field",{attrs:{label:"Оценка качества:",icon:"thumbs_up_down","icon-color":e.form.quality?"positive":"negative",orientation:"horizontal"}},[a("q-select",{attrs:{options:e.options.quality,placeholder:"Выберите оценку качества работы"},model:{value:e.form.quality,callback:function(t){e.$set(e.form,"quality",t)},expression:"form.quality"}})],1),a("q-field",{attrs:{label:"Начало работы:",icon:"today","icon-color":e.form.begin?"positive":"negative",orientation:"horizontal"}},[a("q-datetime",{attrs:{type:"date",format:"DD.MM.YYYY",value:e.form.begin,max:e.form.end,placeholder:"Укажите дату начала работы"},on:{change:function(t){e.form.begin=new Date(t).toDateString()}}})],1),a("q-field",{attrs:{label:"Окончание работы:",icon:"date_range","icon-color":e.form.end?"positive":"negative",orientation:"horizontal"}},[a("q-datetime",{attrs:{type:"date",format:"DD.MM.YYYY",value:e.form.end,disable:!e.form.begin,min:e.form.begin,placeholder:"Укажите дату окончания работы"},on:{change:function(t){e.form.end=new Date(t).toDateString()}}})],1),a("div",{staticClass:"row justify-between q-py-md group q-my-sm round-borders"},[a("q-input",{staticClass:"col shadow-1 justify-center",attrs:{type:"number","hide-underline":"",align:"center","stack-label":"Условия труда"},model:{value:e.form.conditions,callback:function(t){e.$set(e.form,"conditions",t)},expression:"form.conditions"}}),a("q-input",{staticClass:"col shadow-1",attrs:{type:"number","hide-underline":"",align:"center","stack-label":"Премия"},model:{value:e.form.bonus,callback:function(t){e.$set(e.form,"bonus",t)},expression:"form.bonus"}}),a("q-input",{staticClass:"col shadow-1",attrs:{type:"number","hide-underline":"",align:"center","stack-label":"Коэффициент"},model:{value:e.form.coefficient,callback:function(t){e.$set(e.form,"coefficient",t)},expression:"form.coefficient"}})],1),a("q-field",{attrs:{label:"Вид механизма:","icon-color":"green",icon:"settings",orientation:"horizontal"}},[a("q-input",{attrs:{type:"text",autocomplete:"on",placeholder:"Укажите вид механизма"},model:{value:e.form.mechanism,callback:function(t){e.$set(e.form,"mechanism",t)},expression:"form.mechanism"}})],1),a("q-field",{attrs:{label:"Задание на месяц:",icon:"event_note","icon-color":"green",orientation:"horizontal"}},[a("q-input",{attrs:{type:"text",autocomplete:"on",placeholder:"Укажите задание на месяц"},model:{value:e.form.task,callback:function(t){e.$set(e.form,"task",t)},expression:"form.task"}})],1)],1)])]),a("q-step",{attrs:{name:"works",title:"Работы",subtitle:"Перечень работ",order:2,"active-icon":"gavel",icon:"gavel"}},[a("div",{staticClass:"row fit",staticStyle:{"min-height":"66vh"}},[a("q-table",{staticClass:"fit",attrs:{data:e.form.works,columns:e.columns.works,"row-key":"name","table-class":"workTable",dense:"","hide-bottom":""},scopedSlots:e._u([{key:"top-left",fn:function(t){return[a("q-btn",{attrs:{icon:"add",color:"positive",glossy:"",label:"Добавить"},nativeOn:{click:function(t){e.dialogs.work_form=!e.dialogs.work_form}}})]}},{key:"body-cell-options",fn:function(t){return a("q-td",{attrs:{props:t}},[a("q-btn-dropdown",{attrs:{icon:"menu",dense:"",color:"primary",glossy:""}},[a("q-list",{attrs:{link:"",separator:""}},[a("q-item",{nativeOn:{click:function(o){e.editObject(t.row,"work_form")}}},[a("q-item-side",{attrs:{icon:"edit",color:"primary"}}),a("q-item-main",{attrs:{label:"Редактировать"}})],1),a("q-item",{nativeOn:{click:function(o){e.form.works=e.form.works.filter(function(e){return e!==t.row})}}},[a("q-item-side",{attrs:{icon:"delete",color:"negative"}}),a("q-item-main",{attrs:{label:"Удалить"}})],1)],1)],1)],1)}},{key:"bottom-row",fn:function(t){return e.form.works.length>0?[a("q-tr",{staticClass:"bg-grey-2",attrs:{align:"center"}},[a("q-td",[a("strong",[e._v("Итого:")])]),a("q-td",{attrs:{colspan:"7"}}),a("q-td",[a("strong",[e._v(e._s(e.form.amount))])]),a("q-td",{attrs:{colspan:"3"}})],1),a("q-tr",{staticClass:"bg-grey-2",attrs:{align:"center"}},[a("q-td",[a("strong",[e._v("Условия труда:")])]),a("q-td",{attrs:{colspan:"7",align:"left"}},[a("strong",[e._v(e._s(e.form.conditions)+"%")])]),a("q-td",[a("strong",[e._v(e._s(e.form.amount_conditions))])]),a("q-td",{attrs:{colspan:"3"}})],1),e.form.coefficient?a("q-tr",{staticClass:"bg-grey-2",attrs:{align:"center"}},[a("q-td",[a("strong",[e._v("Коэффициент:")])]),a("q-td",{attrs:{colspan:"7",align:"left"}},[a("strong",[e._v(e._s(e.form.coefficient))])]),a("q-td",[a("strong",[e._v(e._s(e.form.amount_coefficient))])]),a("q-td",{attrs:{colspan:"3"}})],1):e._e(),e.form.bonus?a("q-tr",{staticClass:"bg-grey-2",attrs:{align:"center"}},[a("q-td",[a("strong",[e._v("Премия:")])]),a("q-td",{attrs:{colspan:"7",align:"left"}},[a("strong",[e._v(e._s(e.form.bonus)+"%")])]),a("q-td",[a("strong",[e._v(e._s(e.form.amount_bonus))])]),a("q-td",{attrs:{colspan:"3"}})],1):e._e(),a("q-tr",{staticClass:"bg-grey-5",attrs:{align:"center"}},[a("q-td",[a("strong",[e._v("Всего:")])]),a("q-td",{attrs:{colspan:"5"}}),a("q-td",[a("strong",[e._v(e._s(e.form.done_total))])]),a("q-td"),a("q-td",[a("strong",[e._v(e._s(e.form.amount_total))])]),a("q-td",[a("strong",[e._v(e._s(e.form.works.map(function(t){return t.man_days}).reduce(function(t,e){return t+e},0)))])]),a("q-td",[a("strong",[e._v(e._s(e.form.works.map(function(t){return t.auto_days}).reduce(function(t,e){return t+e},0)))])]),a("q-td",[a("strong",[e._v(e._s(e.form.works.map(function(t){return t.days}).reduce(function(t,e){return t+e},0)))])])],1),a("q-tr")]:void 0}}])})],1),a("q-modal",{attrs:{"no-backdrop-dismiss":"","content-css":"max-height:100%;"},on:{hide:function(t){e.resetForm("work_form")}},model:{value:e.dialogs.work_form,callback:function(t){e.$set(e.dialogs,"work_form",t)},expression:"dialogs.work_form"}},[a("q-toolbar",{staticClass:"row justify-end"},[a("q-toolbar-title",[e._v("Добавить работу")]),a("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{flat:"",round:"",dense:"",icon:"close"}})],1),a("div",{staticClass:"q-pa-sm"},[a("q-field",{attrs:{label:"Наименование:"}},[a("q-input",{attrs:{type:"textarea","max-height":10,rows:"3"},model:{value:e.work_form.name,callback:function(t){e.$set(e.work_form,"name",t)},expression:"work_form.name"}})],1),a("q-field",{attrs:{label:"Ед. измерения:"}},[a("q-select",{attrs:{options:e.$store.state.main.units},model:{value:e.work_form.units,callback:function(t){e.$set(e.work_form,"units",t)},expression:"work_form.units"}})],1),a("q-field",{attrs:{label:"Нормы выработки:"}},[a("q-input",{attrs:{type:"number",decimals:1,step:.1,min:0},model:{value:e.work_form.rate,callback:function(t){e.$set(e.work_form,"rate",t)},expression:"work_form.rate"}})],1),a("q-field",{attrs:{label:"Выполнено:"}},[a("q-input",{attrs:{type:"number",decimals:1,step:.1,min:0,readonly:!e.work_form.rate},model:{value:e.work_form.done,callback:function(t){e.$set(e.work_form,"done",t)},expression:"work_form.done"}})],1),a("q-field",{attrs:{label:"Параграф:"}},[a("q-input",{attrs:{type:"text"},model:{value:e.work_form.paragraph,callback:function(t){e.$set(e.work_form,"paragraph",t)},expression:"work_form.paragraph"}})],1),a("q-field",{attrs:{label:"Расценка, руб:"}},[a("q-input",{attrs:{type:"number",decimals:2,step:.1,min:0},model:{value:e.work_form.pricing,callback:function(t){e.$set(e.work_form,"pricing",t)},expression:"work_form.pricing"}})],1),a("q-field",{attrs:{label:"Отработано:"}},[a("q-input",{attrs:{type:"number",decimals:1,step:.1,min:0,"float-label":"Человеко-дней"},model:{value:e.work_form.man_days,callback:function(t){e.$set(e.work_form,"man_days",t)},expression:"work_form.man_days"}}),a("q-input",{attrs:{type:"number",step:.1,min:0,"float-label":"Машино-смен"},model:{value:e.work_form.auto_days,callback:function(t){e.$set(e.work_form,"auto_days",t)},expression:"work_form.auto_days"}}),a("q-input",{attrs:{type:"number",step:.1,min:0,"float-label":"Дней"},model:{value:e.work_form.days,callback:function(t){e.$set(e.work_form,"days",t)},expression:"work_form.days"}})],1),a("div",{staticClass:"row justify-around q-px-xs q-pt-sm"},[a("q-chip",{attrs:{square:"",color:"primary"}},[e._v("Выполнено норм: "+e._s(e.work_form.done_norms))]),a("q-chip",{attrs:{square:"",color:"primary"}},[e._v("Сумма, руб: "+e._s(e.work_form.amount))])],1)],1),a("q-toolbar",{staticClass:"justify-around"},[a("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{label:"Закрыть",color:"negative"}}),a("q-btn",{attrs:{label:"Сохранить",color:"positive",disabled:!e.formIsValid("work_form")},nativeOn:{click:function(t){e.saveObject("work_form","works")}}})],1)],1)],1),a("q-step",{attrs:{name:"tables",title:"Табель",subtitle:"Использование рабочего времени",order:3,"active-icon":"grid_on",icon:"grid_on"}},[a("div",{staticClass:"row",staticStyle:{"min-height":"66vh"}},[a("q-table",{staticClass:"full-width tables",attrs:{data:e.form.tables,columns:e.columns.tables,"row-key":"name",dense:"","hide-bottom":""},scopedSlots:e._u([{key:"top-left",fn:function(t){return[a("q-btn",{attrs:{icon:"add",color:"positive",glossy:"",label:"Добавить"},nativeOn:{click:function(t){e.dialogs.table_form=!e.dialogs.table_form}}})]}},{key:"body-cell-options",fn:function(t){return a("q-td",{attrs:{props:t}},[a("q-btn-dropdown",{attrs:{icon:"menu",dense:"",color:"primary",glossy:""}},[a("q-list",{attrs:{link:"",separator:""}},[a("q-item",{nativeOn:{click:function(o){e.editObject(t.row,"table_form")}}},[a("q-item-side",{attrs:{icon:"edit",color:"primary"}}),a("q-item-main",{attrs:{label:"Редактировать"}})],1),a("q-item",{nativeOn:{click:function(o){e.form.tables=e.form.tables.filter(function(e){return e!==t.row})}}},[a("q-item-side",{attrs:{icon:"delete",color:"negative"}}),a("q-item-main",{attrs:{label:"Удалить"}})],1)],1)],1)],1)}},{key:"bottom-row",fn:function(t){return e.form.tables.length>0?a("q-tr",{staticClass:"bg-grey-5",attrs:{align:"center"}},[a("q-td",[a("strong",[e._v("Итого:")])]),a("q-td",{attrs:{colspan:"2"}}),a("q-td",[a("strong",[e._v(e._s(e.form.hours_total))])]),a("q-td",[a("strong",[e._v(e._s(e.form.days_total))])]),a("q-td",[a("strong",[e._v(e._s(e.form.done_total))])]),a("q-td",[a("strong",[e._v(e._s(e.form.amount))])]),a("q-td",[a("strong",[e._v(e._s(e.form.amount_coefficient))])]),a("q-td",[a("strong",[e._v(e._s(e.form.amount_conditions))])]),a("q-td",[a("strong",[e._v(e._s(e.form.amount_bonus))])]),a("q-td",[a("strong",[e._v(e._s(e.form.amount_total))])])],1):e._e()}}])}),a("q-modal",{attrs:{"no-backdrop-dismiss":""},on:{hide:function(t){e.resetForm("table_form")}},model:{value:e.dialogs.table_form,callback:function(t){e.$set(e.dialogs,"table_form",t)},expression:"dialogs.table_form"}},[a("q-toolbar",{staticClass:"row justify-end"},[a("q-toolbar-title",[e._v("Добавить табель")]),a("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{flat:"",round:"",dense:"",icon:"close"}})],1),a("div",{staticClass:"q-pa-sm",style:e.$root.$q.platform.is.desktop?"max-width: 500px;":"min-height:83vh;"},[a("q-field",{attrs:{label:"Работник:",helper:e.table_form.worker?e.options.workers.find(function(t){return t.id==e.table_form.worker}).position:""}},[a("q-select",{attrs:{options:e.options.workers.filter(function(e){return t.table_form.worker==e.id||!t.form.tables.find(function(t){return t.worker==e.id})}).map(function(t){return{label:t.full_name,value:t.id}}),filter:"","float-label":"Выберите работника","filter-placeholder":"Поиск"},model:{value:e.table_form.worker,callback:function(t){e.$set(e.table_form,"worker",t)},expression:"table_form.worker"}})],1),a("q-field",{attrs:{label:"Разряд:"}},[a("q-input",{attrs:{type:"number",decimals:0,"float-label":"Укажите разряд"},model:{value:e.table_form.rank,callback:function(t){e.$set(e.table_form,"rank",t)},expression:"table_form.rank"}})],1),a("q-field",{attrs:{label:"Отработано часов по числам месяца:",orientation:"vertical"}},[a("q-btn",{attrs:{icon:"add",color:"positive",dense:"",glossy:""},nativeOn:{click:function(t){e.dialogs.workdays=!0}}}),a("div",{staticClass:"shadow-1 q-pa-xs q-mt-sm flex justify-around items-center",staticStyle:{"min-height":"100px"}},e._l(Object.keys(e.table_form.workdays),function(t){return a("q-chip",{key:t,attrs:{closable:"",color:"primary"},on:{hide:function(o){e.$root.$delete(e.table_form.workdays,t)}}},[e._v("\n              "+e._s(t)+" - "+e._s(e.table_form.workdays[t])+"\n            ")])})),a("q-dialog",{attrs:{"no-backdrop-dismiss":""},on:{hide:function(t){e.resetForm("workdays_form")}},scopedSlots:e._u([{key:"buttons",fn:function(t){return[a("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{label:"Закрыть",color:"negative"}}),a("q-btn",{attrs:{label:"Добавить",color:"positive",disabled:!e.formIsValid("workdays_form")},nativeOn:{click:function(t){return e.saveWorkdays(t)}}})]}}]),model:{value:e.dialogs.workdays,callback:function(t){e.$set(e.dialogs,"workdays",t)},expression:"dialogs.workdays"}},[a("div",{attrs:{slot:"body"},slot:"body"},[a("q-datetime",{attrs:{type:"datetime",modal:"","float-label":"Выберите дату и часы",format:"DD.MM.YYYY - HH:mm",clearable:""},model:{value:e.workdays_form.workdays,callback:function(t){e.$set(e.workdays_form,"workdays",t)},expression:"workdays_form.workdays"}})],1)])],1),a("div",{staticClass:"row justify-around q-px-xs q-pt-sm"},[a("q-chip",{attrs:{square:"",color:"primary"}},[e._v("Часов: "+e._s(e.table_form.hours))]),a("q-chip",{attrs:{square:"",color:"primary"}},[e._v("Дней: "+e._s(e.table_form.days))])],1)],1),a("q-toolbar",{staticClass:"justify-around"},[a("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{label:"Закрыть",color:"negative"}}),a("q-btn",{attrs:{label:"Сохранить",color:"positive",disabled:!e.formIsValid("table_form")},nativeOn:{click:function(t){e.saveObject("table_form","tables")}}})],1)],1)],1)]),a("q-step",{attrs:{name:"materials",title:"Материалы",subtitle:"Приходы и расходы материалов",order:4,"active-icon":"swap_horiz",icon:"swap_horiz"}},[a("div",{staticClass:"row",staticStyle:{"min-height":"66vh"}},[a("div",{staticClass:"col-md-6 col-xs-12 flex"},[a("q-table",{staticClass:"fit",attrs:{data:e.form.expenses,columns:e.columns.expenses,"hide-bottom":"",dense:"","row-key":"name"},scopedSlots:e._u([{key:"top",fn:function(t){return a("div",{staticClass:"row fit shadow-1 items-center q-pa-xs bg-tertiary glossy text-white round-borders"},[a("q-btn",{attrs:{icon:"add",color:"positive",dense:"",glossy:"",label:"Добавить"},nativeOn:{click:function(t){e.dialogs.expense_form=!e.dialogs.expense_form}}}),a("span",{staticClass:"q-title col text-center"},[e._v("Расход материалов")])],1)}},{key:"body-cell-options",fn:function(t){return a("q-td",{attrs:{props:t}},[a("q-btn-dropdown",{attrs:{icon:"menu",dense:"",color:"primary",glossy:""}},[a("q-list",{attrs:{link:"",separator:""}},[a("q-item",{nativeOn:{click:function(o){e.editObject(t.row,"expense_form")}}},[a("q-item-side",{attrs:{icon:"edit",color:"primary"}}),a("q-item-main",{attrs:{label:"Редактировать"}})],1),a("q-item",{nativeOn:{click:function(o){e.form.expenses=e.form.expenses.filter(function(e){return e!==t.row})}}},[a("q-item-side",{attrs:{icon:"delete",color:"negative"}}),a("q-item-main",{attrs:{label:"Удалить"}})],1)],1)],1)],1)}}])}),a("q-modal",{attrs:{"no-backdrop-dismiss":""},on:{hide:function(t){e.resetForm("expense_form")}},model:{value:e.dialogs.expense_form,callback:function(t){e.$set(e.dialogs,"expense_form",t)},expression:"dialogs.expense_form"}},[a("q-toolbar",{staticClass:"row justify-end"},[a("q-toolbar-title",[e._v("Добавить расход")]),a("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{flat:"",round:"",dense:"",icon:"close"}})],1),a("div",{staticClass:"q-pa-xs"},[a("q-field",{attrs:{label:"Материал:"}},[a("q-select",{attrs:{options:e.options.materials.map(function(t){return{label:t.name,value:t.id}}),filter:""},model:{value:e.expense_form.material,callback:function(t){e.$set(e.expense_form,"material",t)},expression:"expense_form.material"}})],1),a("q-field",{attrs:{label:"Количество:"}},[a("q-input",{attrs:{type:"number","float-label":"По норме"},model:{value:e.expense_form.quantity_norm,callback:function(t){e.$set(e.expense_form,"quantity_norm",t)},expression:"expense_form.quantity_norm"}}),a("q-input",{attrs:{type:"number","float-label":"Фактически"},model:{value:e.expense_form.quantity_fact,callback:function(t){e.$set(e.expense_form,"quantity_fact",t)},expression:"expense_form.quantity_fact"}})],1),a("q-field",{attrs:{label:"Стоимость, руб:"}},[a("q-input",{attrs:{type:"number",decimals:2,"float-label":"Введите сумму"},model:{value:e.expense_form.cost,callback:function(t){e.$set(e.expense_form,"cost",t)},expression:"expense_form.cost"}})],1)],1),a("q-toolbar",{staticClass:"justify-around"},[a("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{label:"Закрыть",color:"negative"}}),a("q-btn",{attrs:{label:"Сохранить",color:"positive",disabled:!e.formIsValid("expense_form")},nativeOn:{click:function(t){e.saveObject("expense_form","expenses")}}})],1)],1)],1),a("div",{staticClass:"col-md-6 col-xs-12 flex"},[a("q-table",{staticClass:"fit",attrs:{data:e.form.postings,columns:e.columns.postings,"hide-bottom":"",dense:"","row-key":"name"},scopedSlots:e._u([{key:"top",fn:function(t){return a("div",{staticClass:"row fit shadow-1 items-center q-pa-xs bg-tertiary glossy text-white round-borders"},[a("q-btn",{attrs:{icon:"add",color:"positive",dense:"",glossy:"",label:"Добавить"},nativeOn:{click:function(t){e.dialogs.posting_form=!e.dialogs.posting_form}}}),a("span",{staticClass:"q-title col text-center"},[e._v("Приход материалов")])],1)}},{key:"body-cell-options",fn:function(t){return a("q-td",{attrs:{props:t}},[a("q-btn-dropdown",{attrs:{icon:"menu",dense:"",color:"primary",glossy:""}},[a("q-list",{attrs:{link:"",separator:""}},[a("q-item",{nativeOn:{click:function(o){e.editObject(t.row,"posting_form")}}},[a("q-item-side",{attrs:{icon:"edit",color:"primary"}}),a("q-item-main",{attrs:{label:"Редактировать"}})],1),a("q-item",{nativeOn:{click:function(o){e.form.postings=e.form.postings.filter(function(e){return e!==t.row})}}},[a("q-item-side",{attrs:{icon:"delete",color:"negative"}}),a("q-item-main",{attrs:{label:"Удалить"}})],1)],1)],1)],1)}}])}),a("q-modal",{attrs:{"no-backdrop-dismiss":""},on:{hide:function(t){e.resetForm("posting_form")}},model:{value:e.dialogs.posting_form,callback:function(t){e.$set(e.dialogs,"posting_form",t)},expression:"dialogs.posting_form"}},[a("q-toolbar",{staticClass:"row justify-end"},[a("q-toolbar-title",[e._v("Добавить приход")]),a("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{flat:"",round:"",dense:"",icon:"close"}})],1),a("div",{staticClass:"q-pa-xs"},[a("q-field",{attrs:{label:"Мтериал:"}},[a("q-select",{attrs:{options:e.options.materials.map(function(t){return{label:t.name,value:t.id}}),filter:""},model:{value:e.posting_form.material,callback:function(t){e.$set(e.posting_form,"material",t)},expression:"posting_form.material"}})],1),a("q-field",{attrs:{label:"Количество:"}},[a("q-input",{attrs:{type:"number","float-label":"Введите количество"},model:{value:e.posting_form.quantity,callback:function(t){e.$set(e.posting_form,"quantity",t)},expression:"posting_form.quantity"}})],1)],1),a("q-toolbar",{staticClass:"justify-around"},[a("q-btn",{directives:[{name:"close-overlay",rawName:"v-close-overlay"}],attrs:{label:"Закрыть",color:"negative"}}),a("q-btn",{attrs:{label:"Сохранить",color:"positive",disabled:!e.formIsValid("posting_form")},nativeOn:{click:function(t){e.saveObject("posting_form","postings")}}})],1)],1)],1)])]),a("q-step",{attrs:{name:"personal",title:"Перосонал",subtitle:"Ответственные лица",order:5,"active-icon":"people",icon:"people"}},[a("div",{staticClass:"row justify-center"},[a("div",{staticClass:"col-md-5"},[a("q-field",{attrs:{label:"Бригадир:","label-width":"5",orientation:"horizontal",icon:e.form.brigadier?"check_circle":"error","icon-color":e.form.brigadier?"positive":"negative"}},[a("q-select",{attrs:{options:e.options.workers.map(function(t){return{label:t.full_name,value:t.id}}),filter:"","float-label":"Выберите работника","filter-placeholder":"Поиск"},model:{value:e.form.brigadier,callback:function(t){e.$set(e.form,"brigadier",t)},expression:"form.brigadier"}})],1),a("q-field",{attrs:{label:"Наряд выдан:","label-width":"5",orientation:"horizontal",icon:e.form.issued?"check_circle":"error","icon-color":e.form.issued?"positive":"negative"}},[a("q-select",{attrs:{options:e.options.workers.map(function(t){return{label:t.full_name,value:t.id}}),filter:"","float-label":"Выберите работника","filter-placeholder":"Поиск"},model:{value:e.form.issued,callback:function(t){e.$set(e.form,"issued",t)},expression:"form.issued"}})],1),a("q-field",{attrs:{label:"К исполнению принял:","label-width":"5",orientation:"horizontal",icon:e.form.accepted?"check_circle":"error","icon-color":e.form.accepted?"positive":"negative"}},[a("q-select",{attrs:{options:e.options.workers.map(function(t){return{label:t.full_name,value:t.id}}),filter:"","float-label":"Выберите работника","filter-placeholder":"Поиск"},model:{value:e.form.accepted,callback:function(t){e.$set(e.form,"accepted",t)},expression:"form.accepted"}})],1),a("q-field",{attrs:{label:"Работу сдал:","label-width":"5",orientation:"horizontal",icon:e.form.work_passed?"check_circle":"error","icon-color":e.form.work_passed?"positive":"negative"}},[a("q-select",{attrs:{options:e.options.workers.map(function(t){return{label:t.full_name,value:t.id}}),filter:"","float-label":"Выберите работника","filter-placeholder":"Поиск"},model:{value:e.form.work_passed,callback:function(t){e.$set(e.form,"work_passed",t)},expression:"form.work_passed"}})],1),a("q-field",{attrs:{label:"Работу принял:","label-width":"5",orientation:"horizontal",icon:e.form.work_accept?"check_circle":"error","icon-color":e.form.work_accept?"positive":"negative"}},[a("q-select",{attrs:{options:e.options.workers.map(function(t){return{label:t.full_name,value:t.id}}),filter:"","float-label":"Выберите работника","filter-placeholder":"Поиск"},model:{value:e.form.work_accept,callback:function(t){e.$set(e.form,"work_accept",t)},expression:"form.work_accept"}})],1),a("q-field",{attrs:{label:"Ответственный за ведение табеля:","label-width":"5",orientation:"horizontal",icon:e.form.responsible?"check_circle":"error","icon-color":e.form.responsible?"positive":"negative"}},[a("q-select",{attrs:{options:e.options.workers.map(function(t){return{label:t.full_name,value:t.id}}),filter:"","float-label":"Выберите работника","filter-placeholder":"Поиск"},model:{value:e.form.responsible,callback:function(t){e.$set(e.form,"responsible",t)},expression:"form.responsible"}})],1),a("q-field",{attrs:{label:"Расчет составил:","label-width":"5",orientation:"horizontal",icon:e.form.calculated?"check_circle":"error","icon-color":e.form.calculated?"positive":"negative"}},[a("q-select",{attrs:{options:e.options.workers.map(function(t){return{label:t.full_name,value:t.id}}),filter:"","float-label":"Выберите работника","filter-placeholder":"Поиск"},model:{value:e.form.calculated,callback:function(t){e.$set(e.form,"calculated",t)},expression:"form.calculated"}})],1),a("q-field",{attrs:{label:"Принял на ответственное хранение:","label-width":"5",orientation:"horizontal",icon:e.form.deposited?"check_circle":"error","icon-color":e.form.deposited?"positive":"negative"}},[a("q-select",{attrs:{options:e.options.workers.map(function(t){return{label:t.full_name,value:t.id}}),filter:"","float-label":"Выберите работника","filter-placeholder":"Поиск"},model:{value:e.form.deposited,callback:function(t){e.$set(e.form,"deposited",t)},expression:"form.deposited"}})],1)],1)])]),a("q-stepper-navigation",{staticClass:"bg-tertiary q-pa-sm glossy",staticStyle:{margin:"0",height:"10vh"}},[a("div",{staticClass:"row justify-center col-12 group"},[a("q-btn",{staticClass:"text-bold",attrs:{disabled:"main"==e.currentSection,label:"Назад",color:"primary",icon:"arrow_back",glossy:""},on:{click:function(t){e.$refs.stepper.previous()}}}),"personal"==e.currentSection?a("q-btn",{staticClass:"text-bold",attrs:{disabled:!e.stepIsComplete,label:"Сохранить",color:"positive",icon:"save",glossy:""},on:{click:e.saveOutfit}}):a("q-btn",{staticClass:"text-bold",attrs:{label:"Далее",color:"positive",icon:"arrow_forward",glossy:"",disabled:!e.stepIsComplete},on:{click:function(t){e.$refs.stepper.next()}}})],1)])],1)},r=[];a._withStripped=!0;o("hhXQ");var n=o("cDf5"),i=o.n(n),s=(o("Vd3H"),o("yt8O"),o("RW0V"),o("rGqo"),o("f3/d"),o("dRSK"),o("dB3m"),{name:"NewOutfit",data:function(){var t=this;return{currentSection:"main",form:{station:null,departament:null,forestry:null,mechanism:null,event:null,conditions:0,bonus:0,coefficient:0,task:null,begin:null,end:null,quality:null,done_total:0,amount:0,amount_conditions:0,amount_coefficient:0,amount_bonus:0,amount_total:0,hours_total:0,days_total:0,works:[],expenses:[],postings:[],tables:[],brigadier:null,issued:null,accepted:null,work_passed:null,work_accept:null,responsible:null,calculated:null,deposited:null},work_form:{name:null,units:null,rate:null,done:null,paragraph:null,done_norms:null,pricing:null,amount:null,man_days:null,auto_days:null,days:null},table_form:{worker:null,rank:null,workdays:{},hours:null,days:null,tariff_rate:null,by_coefficient:null,by_conditions:null,done:null,bonus:null,total:null},workdays_form:{workdays:null},expense_form:{name:null,units:null,quantity_norm:null,quantity_fact:null,cost:null},posting_form:{name:null,units:null,quantity:null},options:{workers:[],outfit_events:[],stations:[],materials:[],departaments:[{label:"Лес",value:"les"},{label:"Цех",value:"ceh"},{label:"ПХС",value:"phs"},{label:"МТМ",value:"mtm"}],quality:[{label:"Удовлетворительно",value:"good",icon:"thumb_up",leftColor:"positive"},{label:"Неудовлетворительно",value:"bad",icon:"thumb_down",leftColor:"negative"}]},required:{work_form:["name","units","rate","done","paragraph","done_norms","pricing","amount","man_days","days"],table_form:["worker","rank","workdays","hours","days"],workdays_form:["workdays"],expense_form:["material","quantity_norm","quantity_fact"],posting_form:["material","quantity"],main:["station","departament","forestry","event","quality","begin","end"],personal:["brigadier","issued","accepted","work_passed","work_accept","responsible","calculated","deposited"]},dialogs:{work_form:!1,table_form:!1,workdays:!1,expense_form:!1,posting_form:!1},columns:{works:[{name:"options",label:"Опции",align:"center"},{name:"name",label:"Наименование",field:"name",align:"center"},{name:"units",label:"Ед. изм.",field:function(e){return t.$store.state.main.units.find(function(t){return t.value==e.units}).label},align:"center"},{name:"rate",label:"Нормы выработки",field:"rate",align:"center"},{name:"done",label:"Выполнено",field:"done",align:"center"},{name:"paragraph",label:"Параграф",field:"paragraph",align:"center"},{name:"done_norms",label:"Выполнено норм",field:"done_norms",align:"center"},{name:"pricing",label:"Расценка, руб.",field:"pricing",align:"center"},{name:"amount",label:"Сумма, руб.",field:"amount",align:"center"},{name:"man_days",label:"Человеко-дней",field:"man_days",align:"center"},{name:"auto_days",label:"Машино-смен",field:"auto_days",align:"center"},{name:"days",label:"Дней",field:"days",align:"center"}],expenses:[{name:"options",label:"Опции",align:"center"},{name:"material",label:"Материал",field:function(e){return t.options.materials.find(function(t){return t.id==e.material}).name},align:"center"},{name:"units",label:"Ед. изм.",field:function(e){return t.options.materials.find(function(t){return t.id==e.material}).units_full},align:"center"},{name:"quantity_norm",label:"По норме",field:"quantity_norm",align:"center"},{name:"quantity_fact",label:"По факту",field:"quantity_fact",align:"center"},{name:"cost",label:"Стоимость, руб.",field:"cost",align:"center"}],postings:[{name:"options",label:"Опции",align:"center"},{name:"material",label:"Материал",field:function(e){return t.options.materials.find(function(t){return t.id==e.material}).name},align:"center"},{name:"units",label:"Ед. изм.",field:function(e){return t.options.materials.find(function(t){return t.id==e.material}).units_full},align:"center"},{name:"quantity",label:"Количество",field:"quantity",align:"center"}],tables:[{name:"options",label:"Опции",align:"center"},{name:"worker",label:"Работник",field:function(e){return t.options.workers.find(function(t){return t.id==e.worker}).full_name},align:"center"},{name:"rank",label:"Разряд",field:"rank",align:"center"},{name:"hours",label:"Часов",field:"hours",align:"center"},{name:"days",label:"Дней",field:"days",align:"center"},{name:"done",label:"Выполнено норм",field:"done",align:"center"},{name:"tariff_rate ",label:"Тарифная ставка",field:"tariff_rate",align:"center"},{name:"by_coefficient ",label:"По коэффициенту",field:"by_coefficient",align:"center"},{name:"by_conditions ",label:"По условиям труда",field:"by_conditions",align:"center"},{name:"bonus",label:"Премия",field:"bonus",align:"center"},{name:"total",label:"Всего",field:"total",align:"center"}]}}},methods:{getData:function(t,e){var o=this;this.$axios.get("/api/v1/"+t+"/",{params:e}).then(function(e){o.options[t]=e.data[t]}).catch(function(t){console.log(t.message)})},editObject:function(t,e){var o=this;Object.keys(t).forEach(function(a){return o[e][a]=t[a]}),this.dialogs[e]=!0},saveObject:function(t,e){if(this.formIsValid(t)){var o=JSON.parse(JSON.stringify(this[t]));o.hasOwnProperty("__index")&&null!=o["__index"]?(this.form[e][o["__index"]]=o,this.form[e].sort()):this.form[e].push(o),this.dialogs[t]=!1}},saveWorkdays:function(){var t=new Date(this.workdays_form.workdays).getDate(),e=new Date(this.workdays_form.workdays).getHours();this.$root.$set(this.table_form.workdays,t,e),this.dialogs.workdays=!1},formIsValid:function(t){var e=this;return!!this.required[t].every(function(o){return null!==e[t][o]&&""!==e[t][o]})},resetForm:function(t){var e=this;t&&e[t]&&Object.keys(e[t]).forEach(function(o){Array.isArray(e[t][o])?e[t][o]=[]:e[t][o]&&"object"===i()(e[t][o])&&e[t][o].constructor===Object?e[t][o]={}:e[t][o]=null})},saveOutfit:function(){var t=this,e=JSON.stringify(this.form);this.$axios.post("/api/v1/outfit/",e).then(function(e){t.$router.push("/docs/outfits/")}).catch(function(e){t.$root.handleError(e.message)})}},computed:{stepIsComplete:function(){var t=this,e=!1;switch(this.currentSection){case"main":this.required.main.every(function(e){return null!==t.form[e]&&""!==t.form[e]})&&(e=!0);break;case"works":this.form.works.length>0&&(e=!0);break;case"tables":this.form.tables.length>0&&(e=!0);break;case"materials":e=!0;break;case"personal":this.required.personal.every(function(e){return null!==t.form[e]&&""!==t.form[e]})&&(e=!0);break}return e}},mounted:function(){this.getData("outfit_events"),this.getData("stations"),this.getData("materials")},watch:{"table_form.workdays":function(t){var e=0;this.table_form.days=Object.keys(t).length||null;for(var o=0;o<Object.values(t).length;o++)e+=Object.values(t)[o];this.table_form.hours=e||null},"form.bonus":function(t){this.form.works.sort()},"form.conditions":function(t){this.form.works.sort()},"form.coefficient":function(t){this.form.works.sort()},"form.works":function(t){if(t.length>0){for(var e=0,o=0,a=this.form.conditions||0,r=this.form.coefficient||0,n=this.form.bonus||0,i=0;i<t.length;i++)e+=parseFloat(t[i].done_norms),o+=parseFloat(t[i].amount);this.form.done_total=e.toFixed(2),this.form.amount=o.toFixed(2),this.form.amount_conditions=(o*a/100).toFixed(2),this.form.amount_coefficient=r?(o*r).toFixed(2):0,this.form.amount_bonus=(o*n/100).toFixed(2),this.form.amount_total=(o+parseFloat(this.form.amount_conditions)+parseFloat(this.form.amount_coefficient)+parseFloat(this.form.amount_bonus)).toFixed(2)}else this.form.done_total=this.form.amount=this.form.amount_conditions=this.form.amount_coefficient=this.form.amount_bonus=this.form.amount_total=0;this.form.tables.sort()},"work_form.rate":function(t){t&&(this.work_form.done_norms=(this.work_form.done/t).toFixed(2))},"work_form.pricing":function(t){t&&(this.work_form.amount=(t*this.work_form.done_norms).toFixed(2))},"work_form.done":function(t){t&&(this.work_form.done_norms=(t/this.work_form.rate).toFixed(2))},"work_form.done_norms":function(t){t&&(this.work_form.amount=(this.work_form.pricing*t).toFixed(2))},"form.station":function(t){t&&this.getData("workers",{station:t})},"form.tables":function(t){for(var e=0,o=0,a=0;a<t.length;a++)e+=t[a].hours,o+=t[a].days;this.form.hours_total=e,this.form.days_total=o;for(a=0;a<t.length;a++){var r=t[a].hours/e;t[a].tariff_rate=(parseFloat(this.form.amount)*r).toFixed(2),t[a].by_conditions=(parseFloat(this.form.amount_conditions)*r).toFixed(2),t[a].by_coefficient=(parseFloat(this.form.amount_coefficient)*r).toFixed(2),t[a].done=(parseFloat(this.form.done_total)*r).toFixed(2),t[a].bonus=(parseFloat(this.form.amount_bonus)*r).toFixed(2),t[a].total=(parseFloat(this.form.amount_total)*r).toFixed(2)}}}}),l=s,c=(o("8z5z"),o("KHd+")),f=Object(c["a"])(l,a,r,!1,null,null,null);e["default"]=f.exports},"7u4A":function(t,e,o){},"8z5z":function(t,e,o){"use strict";var a=o("7u4A"),r=o.n(a);r.a},UExd:function(t,e,o){var a=o("DVgA"),r=o("aCFj"),n=o("UqcF").f;t.exports=function(t){return function(e){var o,i=r(e),s=a(i),l=s.length,c=0,f=[];while(l>c)n.call(i,o=s[c++])&&f.push(t?[o,i[o]]:i[o]);return f}}},hhXQ:function(t,e,o){var a=o("XKFU"),r=o("UExd")(!1);a(a.S,"Object",{values:function(t){return r(t)}})}}]);