(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[30],{Qmyi:function(t,s,a){"use strict";a.r(s);var e=function(){var t=this,s=t.$createElement,a=t._self._c||s;return t.table?a("q-layout",{attrs:{id:"wt-print"}},[a("q-page-sticky",{staticClass:"print-hide z-max",attrs:{position:"top-left"}},[a("div",{staticClass:"group"},[a("q-btn",{staticClass:"rotate-180",attrs:{icon:"forward",round:"",color:"primary"},nativeOn:{click:function(s){t.$router.push({name:"WorkTimeTable"})}}}),a("q-btn",{attrs:{icon:"print",round:"",color:"positive"},nativeOn:{click:function(s){return t.print(s)}}})],1)]),a("div",{staticClass:"page"},[a("div",{staticClass:"row"},[a("div",{staticClass:"col-9",staticStyle:{"font-size":"11px"}},[a("div",{staticClass:"row justify-center"},[a("span",{staticClass:"text-bold"},[t._v("\n\t\t\t\t\t\tТабель № "),a("span",{staticClass:"q-px-md",staticStyle:{"border-bottom":"1px solid"}},[t._v(t._s(t.table.id))]),a("br"),a("br"),t._v("\n\t\t\t\t\t\tучета использования рабочего времени\n\t\t\t\t\t")])]),a("div",{staticClass:"row justify-center q-pt-md"},[a("span",[t._v("за\n\t\t\t\t\t\t"),a("span",{staticClass:"bb q-mx-sm q-px-sm"},[t._v(t._s(new Date(t.table.date).toLocaleDateString("RU",{month:"long"})))]),a("span",{staticClass:"bb q-px-sm"},[t._v(t._s(new Date(t.table.date).getFullYear()))]),t._v("г.\n\t\t\t\t\t")])]),a("div",{staticClass:"row q-pt-md"},[a("div",{staticClass:"col-3 text-left q-pt-xs"},[t._v("Учреждение")]),a("div",{staticClass:"col-9 bb q-pt-xs"},[t._v(t._s(t.table.organization.name))]),a("div",{staticClass:"col-3 text-left q-pt-xs"},[t._v("Структурное подразделение")]),a("div",{staticClass:"col-9 bb q-pt-xs"},[t._v(t._s(t.table.station.name))]),a("div",{staticClass:"col-3 text-left q-pt-xs"},[t._v("Отдел")]),a("div",{staticClass:"col-9 bb q-pt-xs"},[t._v(t._s(t.table.departament_full))]),a("div",{staticClass:"col-3 text-left q-pt-xs"},[t._v("Вид табеля")]),a("div",{staticClass:"col-9 bb q-mt-xs"},[t._v("0"),a("span",{staticClass:"ut"},[t._v("(первичный - 0, коректирующий - 1, 2 и т.д.)")])])])]),a("div",{staticClass:"col-3 flex items-end justify-end"},[a("table",{staticClass:"mini-table",staticStyle:{"font-size":"9px"},attrs:{align:"right",cellspacing:"0"}},[a("tbody",[a("tr",[a("td",[t._v(" ")]),a("td",{staticStyle:{border:"1px solid"}},[t._v("Коды")])]),a("tr",[a("td",{staticClass:"text-right"},[t._v("Форма по ОКУД")]),a("td",[t._v("0504421")])]),a("tr",[a("td",{staticClass:"text-right"},[t._v("Дата")]),a("td",[t._v(t._s(new Date(t.table.created_date).toLocaleDateString("RU")))])]),a("tr",[a("td",{staticClass:"text-right"},[t._v("по ОКПО")]),a("td",[t._v(" ")])]),a("tr",[a("td",[t._v(" ")]),a("td",[t._v(" ")])]),a("tr",[a("td",{staticClass:"text-right"},[t._v("Номер коректировки")]),a("td",[t._v(" ")])]),a("tr",[a("td",{staticClass:"text-right"},[t._v("Дата формирования документа")]),a("td",[t._v(t._s(new Date(t.table.created_date).toLocaleDateString("RU")))])])])])])]),a("div",{staticClass:"row q-pt-lg"},[a("table",{staticClass:"full-width worktime-table",attrs:{cellspacing:"0",border:"1"}},[a("thead",[a("tr",[a("th",{attrs:{rowspan:"2"}},[t._v("Фамилия, имя,"),a("br"),t._v("отчество")]),a("th",{attrs:{rowspan:"2",width:"45px"}},[t._v("Учетный"),a("br"),t._v("номер")]),a("th",{attrs:{rowspan:"2",width:"80px"}},[t._v("Должность"),a("br"),t._v("(профессия)")]),a("th",{attrs:{colspan:"32"}},[t._v("Числа месяца")])]),a("tr",[t._l(31,function(s){return a("th",{attrs:{width:"25px"}},[t._v(t._s(s))])}),a("th",{attrs:{width:"45px"}},[t._v("\n\t\t\t\t\t\t\tВсего дней (часов) явок (неявок) за месяц\n\t\t\t\t\t\t")])],2)]),a("tbody",[t._l(t.table.entries.slice(0,25),function(s,e){return a("tr",{attrs:{"row-key":"id"}},[a("td",[t._v(t._s(s.worker.full_name))]),a("td",[t._v(t._s(e+1))]),a("td",[t._v(t._s(s.worker.position))]),t._l(31,function(e){return a("td",[t._v(t._s(s.workdays[e]))])}),a("td",[t._v(t._s(Object.values(s.workdays).reduce(function(t,s){return parseFloat(t)+parseFloat(s)},0)))])],2)}),t.table.entries.length<25?t._l(25-t.table.entries.length,function(s){return a("tr",{attrs:{"row-key":s}},t._l(35,function(s){return a("td",[t._v(" ")])}))}):t._e()],2),t.table.entries.length<26?a("tfoot",[a("tr",[a("th",[t._v("Итого:")]),a("th",[t._v(t._s(t.table.entries.length))]),t._l(32,function(t){return a("th")}),a("th",[t._v(t._s(t.table.hours))])],2)]):t._e()])]),t.table.entries.length<26?a("div",{staticClass:"row q-pt-md"},[a("div",{staticClass:"col"},[a("div",{staticClass:"row"},[a("span",{staticClass:"inline-block text-left q-px-sm"},[t._v("\n\t\t\t\t\t\tОтветственный"),a("br"),t._v("\n\t\t\t\t\t\tисполнитель\n\t\t\t\t\t")]),a("span",{staticClass:"bb q-px-sm",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.responsible.position)),a("span",{staticClass:"ut"},[t._v("(должность)")])]),a("span",{staticClass:"bb q-px-lg q-mx-sm",staticStyle:{"min-width":"100px"}},[t._v(" "),a("span",{staticClass:"ut"},[t._v("(подпись)")])]),a("span",{staticClass:"bb",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.responsible.full_name)),a("span",{staticClass:"ut"},[t._v("(расшифровка подписи)")])])]),a("div",{staticClass:"row q-pt-md"},[a("span",{staticClass:"inline-block text-left q-px-sm"},[t._v("\n\t\t\t\t\t\tИсполнитель\n\t\t\t\t\t")]),a("span",{staticClass:"bb q-px-sm",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.performer.position)),a("span",{staticClass:"ut"},[t._v("(должность)")])]),a("span",{staticClass:"bb q-px-lg q-mx-sm",staticStyle:{"min-width":"100px"}},[t._v(" "),a("span",{staticClass:"ut"},[t._v("(подпись)")])]),a("span",{staticClass:"bb",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.performer.full_name)),a("span",{staticClass:"ut"},[t._v("(расшифровка подписи)")])])]),a("div",{staticClass:"row q-pt-md q-px-sm"},[t._v('\n\t\t\t\t\t"'),a("span",{staticClass:"bb q-px-sm"},[t._v(t._s(new Date(t.table.created_date).getDate()))]),t._v('"\n\t\t\t\t\t'),a("span",{staticClass:"bb q-px-sm q-mx-sm"},[t._v(t._s(new Date(t.table.created_date).toLocaleDateString("RU",{month:"long"})))]),a("span",{staticClass:"bb q-px-sm"},[t._v(t._s(new Date(t.table.created_date).getFullYear()))]),t._v("г.\n\t\t\t\t")])]),a("div",{staticClass:"col"},[a("div",{staticClass:"row justify-center"},[a("span",{staticClass:"text-bold",staticStyle:{"font-size":"10px"}},[t._v("Отметка бухгалтерии о принятии настоящего табеля")])]),a("div",{staticClass:"row q-pt-md"},[a("span",{staticClass:"inline-block text-left q-px-sm"},[t._v("\n\t\t\t\t\t\tИсполнитель\n\t\t\t\t\t")]),a("span",{staticClass:"bb q-px-sm",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.performer.position)),a("span",{staticClass:"ut"},[t._v("(должность)")])]),a("span",{staticClass:"bb q-px-lg q-mx-sm",staticStyle:{"min-width":"100px"}},[t._v(" "),a("span",{staticClass:"ut"},[t._v("(подпись)")])]),a("span",{staticClass:"bb",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.performer.full_name)),a("span",{staticClass:"ut"},[t._v("(расшифровка подписи)")])])]),a("div",{staticClass:"row q-pt-md q-px-sm"},[t._v('\n\t\t\t\t\t"'),a("span",{staticClass:"bb q-px-sm"},[t._v(t._s(new Date(t.table.created_date).getDate()))]),t._v('"\n\t\t\t\t\t'),a("span",{staticClass:"bb q-px-sm q-mx-sm"},[t._v(t._s(new Date(t.table.created_date).toLocaleDateString("RU",{month:"long"})))]),a("span",{staticClass:"bb q-px-sm"},[t._v(t._s(new Date(t.table.created_date).getFullYear()))]),t._v("г.\n\t\t\t\t")])])]):t._e()]),t.table.entries.length>25?a("div",{staticClass:"page"},[a("div",{staticClass:"row q-pt-lg"},[a("table",{staticClass:"full-width worktime-table q-mt-md",attrs:{cellspacing:"0",border:"1"}},[a("thead",[a("tr",[a("th",{attrs:{rowspan:"2"}},[t._v("Фамилия, имя,"),a("br"),t._v("отчество")]),a("th",{attrs:{rowspan:"2",width:"45px"}},[t._v("Учетный"),a("br"),t._v("номер")]),a("th",{attrs:{rowspan:"2",width:"80px"}},[t._v("Должность"),a("br"),t._v("(профессия)")]),a("th",{attrs:{colspan:"32"}},[t._v("Числа месяца")])]),a("tr",[t._l(31,function(s){return a("th",{attrs:{width:"25px"}},[t._v(t._s(s))])}),a("th",{attrs:{width:"45px"}},[t._v("\n\t\t\t\t\t\t\tВсего дней (часов) явок (неявок) за месяц\n\t\t\t\t\t\t")])],2)]),a("tbody",t._l(t.table.entries.slice(25,70),function(s,e){return a("tr",{attrs:{"row-key":"id"}},[a("td",[t._v(t._s(s.worker.full_name))]),a("td",[t._v(t._s(e+31))]),a("td",[t._v(t._s(s.worker.position))]),t._l(31,function(e){return a("td",[t._v(t._s(s.workdays[e]))])}),a("td",[t._v(t._s(Object.values(s.workdays).reduce(function(t,s){return parseFloat(t)+parseFloat(s)},0)))])],2)})),t.table.entries.length<26?a("tfoot",[a("tr",[a("th",[t._v("Итого:")]),a("th",[t._v(t._s(t.table.entries.length))]),t._l(32,function(t){return a("th")}),a("th",[t._v(t._s(t.table.hours))])],2)]):t._e()])]),t.table.entries.length>25?a("div",{staticClass:"row q-pt-md"},[a("div",{staticClass:"col"},[a("div",{staticClass:"row"},[a("span",{staticClass:"inline-block text-left q-px-sm"},[t._v("\n\t\t\t\t\t\tОтветственный"),a("br"),t._v("\n\t\t\t\t\t\tисполнитель\n\t\t\t\t\t")]),a("span",{staticClass:"bb q-px-sm",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.responsible.position)),a("span",{staticClass:"ut"},[t._v("(должность)")])]),a("span",{staticClass:"bb q-px-lg q-mx-sm",staticStyle:{"min-width":"100px"}},[t._v(" "),a("span",{staticClass:"ut"},[t._v("(подпись)")])]),a("span",{staticClass:"bb",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.responsible.full_name)),a("span",{staticClass:"ut"},[t._v("(расшифровка подписи)")])])]),a("div",{staticClass:"row q-pt-md"},[a("span",{staticClass:"inline-block text-left q-px-sm"},[t._v("\n\t\t\t\t\t\tИсполнитель\n\t\t\t\t\t")]),a("span",{staticClass:"bb q-px-sm",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.performer.position)),a("span",{staticClass:"ut"},[t._v("(должность)")])]),a("span",{staticClass:"bb q-px-lg q-mx-sm",staticStyle:{"min-width":"100px"}},[t._v(" "),a("span",{staticClass:"ut"},[t._v("(подпись)")])]),a("span",{staticClass:"bb",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.performer.full_name)),a("span",{staticClass:"ut"},[t._v("(расшифровка подписи)")])])]),a("div",{staticClass:"row q-pt-md q-px-sm"},[t._v('\n\t\t\t\t\t"'),a("span",{staticClass:"bb q-px-sm"},[t._v(t._s(new Date(t.table.created_date).getDate()))]),t._v('"\n\t\t\t\t\t'),a("span",{staticClass:"bb q-px-sm q-mx-sm"},[t._v(t._s(new Date(t.table.created_date).toLocaleDateString("RU",{month:"long"})))]),a("span",{staticClass:"bb q-px-sm"},[t._v(t._s(new Date(t.table.created_date).getFullYear()))]),t._v("г.\n\t\t\t\t")])]),a("div",{staticClass:"col"},[a("div",{staticClass:"row justify-center"},[a("span",{staticClass:"text-bold",staticStyle:{"font-size":"10px"}},[t._v("Отметка бухгалтерии о принятии настоящего табеля")])]),a("div",{staticClass:"row q-pt-md"},[a("span",{staticClass:"inline-block text-left q-px-sm"},[t._v("\n\t\t\t\t\t\tИсполнитель\n\t\t\t\t\t")]),a("span",{staticClass:"bb q-px-sm",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.performer.position)),a("span",{staticClass:"ut"},[t._v("(должность)")])]),a("span",{staticClass:"bb q-px-lg q-mx-sm",staticStyle:{"min-width":"100px"}},[t._v(" "),a("span",{staticClass:"ut"},[t._v("(подпись)")])]),a("span",{staticClass:"bb",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.table.performer.full_name)),a("span",{staticClass:"ut"},[t._v("(расшифровка подписи)")])])]),a("div",{staticClass:"row q-pt-md q-px-sm"},[t._v('\n\t\t\t\t\t"'),a("span",{staticClass:"bb q-px-sm"},[t._v(t._s(new Date(t.table.created_date).getDate()))]),t._v('"\n\t\t\t\t\t'),a("span",{staticClass:"bb q-px-sm q-mx-sm"},[t._v(t._s(new Date(t.table.created_date).toLocaleDateString("RU",{month:"long"})))]),a("span",{staticClass:"bb q-px-sm"},[t._v(t._s(new Date(t.table.created_date).getFullYear()))]),t._v("г.\n\t\t\t\t")])])]):t._e()]):t._e()],1):t._e()},i=[];e._withStripped=!0;var l={name:"WorkTimeTablePrint",props:{id:{required:!0}},data:function(){return{table:null}},methods:{getTable:function(){var t=this;this.$axios.get("/api/v1/worktime_tables/"+this.id+"/").then(function(s){t.table=s.data}).catch(function(t){})},print:function(){window.print()}},mounted:function(){this.getTable()}},n=l,r=(a("jsSv"),a("KHd+")),c=Object(r["a"])(n,e,i,!1,null,null,null);s["default"]=c.exports},asCz:function(t,s,a){},jsSv:function(t,s,a){"use strict";var e=a("asCz"),i=a.n(e);i.a}}]);