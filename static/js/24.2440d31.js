(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[24],{"7c4c":function(t,s,a){},IVl5:function(t,s,a){"use strict";var i=a("7c4c"),o=a.n(i);o.a},xDAa:function(t,s,a){"use strict";a.r(s);var i=function(){var t=this,s=t.$createElement,a=t._self._c||s;return a("q-layout",[a("q-page-container",[t.outfit?a("q-page",{staticStyle:{"font-family":"Times New Roman","font-size":"10px"}},[a("q-page-sticky",{staticClass:"print-hide",attrs:{position:"top-left",offset:[18,18]}},[a("div",{staticClass:"group"},[a("q-btn",{attrs:{round:"",glossy:"",color:"primary",size:"md",icon:"reply",title:"Назад"},on:{click:function(s){t.$router.go(-1)}}}),a("q-btn",{attrs:{round:"",glossy:"",color:"positive",size:"md",icon:"print",title:"Печать"},nativeOn:{click:function(s){return t.print(s)}}})],1)]),a("div",{staticClass:"page"},[a("div",{staticClass:"row justify-end"},[t._v("\n          Форма № Т-55\n        ")]),a("div",{staticClass:"row justify-end"},[a("div",{staticClass:"col-auto text-center"},[a("span",[t._v("УТВЕРЖДАЮ")]),a("br"),a("u",{staticClass:"pos ws-pre relative-position"},[t._v('  И. о. директора Тарасовского ГАУ РО "Лес" ')]),a("br"),a("br"),a("u",{staticClass:"sign ws-pre relative-position"},[t._v("                     ")]),a("u",{staticClass:"sign-trans ws-pre relative-position"},[t._v("        Тульнов В.В.        ")]),a("br"),a("br"),a("pre",[t._v('"'),a("u",[t._v("   ")]),t._v('" '),a("u",[t._v("           ")]),t._v(" "),a("u",[t._v("      ")]),t._v("г.")])])]),a("div",{staticClass:"row justify-center"},[a("div",{staticClass:"col-auto"},[a("span",{staticClass:"ws-pre"},[a("strong",[t._v("НАРЯД - АКТ")]),t._v(" № "),a("u",[t._v(" "+t._s(t.outfit.id)+" ")]),t._v(' от "'),a("u",[t._v(" "+t._s(new Date(t.outfit.date).getDate())+" ")]),t._v('" '),a("u",[t._v("  "+t._s(new Date(t.outfit.date).toLocaleDateString("ru-RU",{month:"long"}))+"  ")]),a("u",[t._v(t._s(new Date(t.outfit.date).getFullYear()))]),t._v(" г.")]),a("br"),a("span",{staticClass:"self-start"},[t._v("на выполнение работ")])])]),a("div",{staticClass:"row q-pa-sm"},[a("div",{staticClass:"col-12"},[a("span",[t._v("Участок: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.station.name)+" ")])]),t._v("    \n            "),a("span",[t._v("Отдел: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.departament_full)+" ")])]),t._v("    \n            "),a("span",[t._v("Бригада: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.brigadier.full_name)+" ")])]),t._v("    \n            "),a("span",[t._v("Кол-во чел: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.tables.length)+" ")])]),t._v("    \n            "),a("span",[t._v("Лесничество: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.forestry)+" ")])]),t._v("    \n            "),a("span",[t._v("Вид механизма: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.mechanism)+" ")])]),t._v("    \n          ")]),a("div",{staticClass:"col-12"},[a("span",[t._v("Наименование мероприятия: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.event.full_name)+" ")])]),t._v("    \n            "),a("span",[t._v("Условия труда: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.conditions)+" ")])]),t._v("    \n            "),a("span",[t._v("Коэффициент: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.coefficient)+" ")])]),t._v("    \n            "),a("span",[t._v("Премия: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.bonus)+" ")])]),t._v("    \n            "),a("span",[t._v("Задание на месяц: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(t.outfit.task)+" ")])]),t._v("    \n          ")]),a("div",{staticClass:"col-12"},[a("span",[t._v("Начало работы: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(new Date(t.outfit.begin).toLocaleDateString())+" ")])]),t._v("    \n            "),a("span",[t._v("Окончание работы: "),a("u",{staticClass:"ws-pre"},[t._v(" "+t._s(new Date(t.outfit.end).toLocaleDateString())+" ")])])])]),a("div",{staticClass:"row"},[a("table",{staticClass:"fit tables",attrs:{border:"1",cellspacing:"0"}},[a("thead",[a("tr",[a("th",{attrs:{rowspan:"3"}},[t._v("Наименование работ(описание)")]),a("th",{attrs:{rowspan:"3"}},[t._v("Ед. изм.")]),a("th",{attrs:{colspan:"2"}},[t._v("Объем работы")]),a("th",{attrs:{rowspan:"3"}},[t._v("Параграф"),a("br"),t._v("справ."),a("br"),t._v("норм")]),a("th",{attrs:{rowspan:"3"}},[t._v("Выполнено"),a("br"),t._v("норм")]),a("th",{attrs:{rowspan:"3"}},[t._v("Расценка,"),a("br"),t._v("руб.")]),a("th",{attrs:{rowspan:"3"}},[t._v("Сумма,"),a("br"),t._v("руб.")]),a("th",{attrs:{colspan:"3"}},[t._v("Отработано")])]),a("tr",[a("th",[t._v("Нормы выработки")]),a("th",[t._v("Выполнено")]),a("th",[t._v("Чел-"),a("br"),t._v("дней")]),a("th",[t._v("Машино-"),a("br"),t._v("смен")]),a("th",[t._v("Кол-во"),a("br"),t._v("дней")])])]),a("tbody",[t._l(t.outfit.works,function(s){return a("tr",[a("td",{staticClass:"text-left"},[t._v(t._s(s.name))]),a("td",[t._v(t._s(t.options.units.find(function(t){return t.value==s.units}).label))]),a("td",[t._v(t._s(s.rate))]),a("td",[t._v(t._s(s.done))]),a("td",[t._v(t._s(s.paragraph))]),a("td",[t._v(t._s(s.done_norms))]),a("td",[t._v(t._s(s.pricing))]),a("td",[t._v(t._s(s.amount))]),a("td",[t._v(t._s(s.man_days))]),a("td",[t._v(t._s(parseFloat(s.auto_days)||null))]),a("td",[t._v(t._s(parseFloat(s.days)||null))])])}),t._l(11-t.outfit.works.length,function(s){return a("tr",[a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")])])})],2),a("tfoot",{staticStyle:{"font-weight":"bold"}},[a("tr",[a("td",[t._v("Итого:")]),a("td"),a("td"),a("td"),a("td"),a("td"),a("td"),a("td",[t._v(t._s(t.outfit.amount))]),a("td"),a("td"),a("td")]),t.outfit.conditions?a("tr",[a("td",[t._v("\n                  Условия труда: "+t._s(t.outfit.conditions)+"\n                ")]),a("td"),a("td"),a("td"),a("td"),a("td"),a("td"),a("td",[t._v(t._s(t.outfit.amount_conditions))]),a("td"),a("td"),a("td")]):t._e(),t.outfit.coefficient?a("tr",[a("td",[t._v("\n                  Коэффициент: "+t._s(parseFloat(t.outfit.coefficient))+"\n                ")]),a("td"),a("td"),a("td"),a("td"),a("td"),a("td"),a("td",[t._v(t._s(t.outfit.amount_coefficient))]),a("td"),a("td"),a("td")]):t._e(),t.outfit.bonus?a("tr",[a("td",[t._v("\n                  Премия: "+t._s(parseFloat(t.outfit.bonus))+" %\n                ")]),a("td"),a("td"),a("td"),a("td"),a("td"),a("td"),a("td",[t._v(t._s(t.outfit.amount_bonus))]),a("td"),a("td"),a("td")]):t._e(),a("tr",[a("td",[t._v("\n                  Всего:\n                ")]),a("td"),a("td"),a("td"),a("td"),a("td",[t._v(t._s(t.outfit.done_total))]),a("td"),a("td",[t._v(t._s(t.outfit.amount_total))]),a("td",[t._v(t._s(t.outfit.works.map(function(t){return t.man_days}).reduce(function(t,s){return t+s})))]),a("td",[t._v(t._s(t.outfit.works.map(function(t){return t.auto_days}).reduce(function(t,s){return t+s})))]),a("td",[t._v(t._s(parseFloat(t.outfit.works.map(function(t){return t.days}).reduce(function(t,s){return t+s}))||null))])])])])]),a("div",{staticClass:"row q-py-sm"},[a("table",{staticClass:"tables",attrs:{border:"1",cellspacing:"0"}},[a("thead",[a("tr",[a("th",{attrs:{colspan:"5"}},[t._v("РАСХОД СЫРЬЯ, МАТЕРИАЛОВ И ОТХОДОВ ПРОИЗВОДСТВА")])]),a("tr",[a("th",{attrs:{rowspan:"2"}},[t._v("Наименование сырья, материалов и отходов производства")]),a("th",{attrs:{rowspan:"2"}},[t._v("Ед. изм.")]),a("th",{attrs:{colspan:"2"}},[t._v("Количество")]),a("th",{attrs:{rowspan:"2"}},[t._v("Стоимость, руб.")])]),a("tr",[a("th",[t._v("По норме")]),a("th",[t._v("Фактическая")])])]),a("tbody",{staticClass:"text-center"},[t._l(t.outfit.expenses,function(s){return a("tr",[a("td",{staticClass:"text-left"},[t._v("\n                  "+t._s(s.material.name)+"\n                ")]),a("td",[t._v("\n                  "+t._s(s.material.units_full)+"\n                ")]),a("td",[t._v("\n                  "+t._s(s.quantity_norm)+"\n                ")]),a("td",[t._v("\n                  "+t._s(s.quantity_fact)+"\n                ")]),a("td",[t._v("\n                  "+t._s(s.cost)+"\n                ")])])}),t._l(3-t.outfit.expenses.length,function(s){return a("tr",[a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")])])})],2)])]),a("div",{staticClass:"row flex-center",staticStyle:{outline:"1px solid"}},[a("div",{staticClass:"col-6"},[a("div",{staticClass:"row q-pa-sm"},[t._v("Наряд выдан: "),a("span",{staticClass:"text-center pos relative-position q-mr-sm bor-bot",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.outfit.issued.position))]),a("span",{staticClass:"sign relative-position q-mr-sm bor-bot",staticStyle:{width:"100px"}}),a("span",{staticClass:"text-center sign-trans relative-position bor-bot",staticStyle:{width:"150px"}},[t._v(t._s(t.outfit.issued.full_name))])]),a("div",{staticClass:"row q-pa-sm"},[t._v("Выполненную работу сдал: \n              "),a("span",{staticClass:"pos relative-position q-mr-sm bor-bot text-center",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.outfit.work_passed.position))]),a("span",{staticClass:"sign relative-position q-mr-sm bor-bot",staticStyle:{width:"100px"}}),a("span",{staticClass:"text-center sign-trans relative-position bor-bot",staticStyle:{width:"150px"}},[t._v(t._s(t.outfit.work_passed.full_name))])])]),a("div",{staticClass:"col-6",staticStyle:{outline:"1px solid"}},[a("div",{staticClass:"row q-pa-sm"},[t._v("К исполнению принял: \n              "),a("span",{staticClass:"text-center q-px-sm pos relative-position q-mr-sm bor-bot",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.outfit.accepted.position))]),a("span",{staticClass:"sign relative-position q-mr-sm bor-bot",staticStyle:{width:"100px"}}),a("span",{staticClass:"text-center sign-trans relative-position bor-bot",staticStyle:{width:"150px"}},[t._v(t._s(t.outfit.accepted.full_name))])]),a("div",{staticClass:"row q-pa-sm"},[t._v("Работу принял: \n              "),a("span",{staticClass:"pos q-px-sm text-center relative-position q-mr-sm bor-bot",staticStyle:{"min-width":"100px"}},[t._v(t._s(t.outfit.work_accept.position))]),a("span",{staticClass:"sign relative-position q-mr-sm bor-bot",staticStyle:{width:"100px"}}),a("span",{staticClass:"text-center sign-trans relative-position bor-bot",staticStyle:{width:"150px"}},[t._v(t._s(t.outfit.work_accept.full_name))])]),a("div",{staticClass:"row q-pa-sm"},[a("span",{staticClass:"bor-bot q-px-sm"},[t._v(t._s(t.outfit.quality_display))]),t._v(" (оценка качества произведенных работ и продукций)")])])])]),a("div",{staticClass:"pagebreak"}),a("div",{staticClass:"page"},[a("div",{staticClass:"row justify-end"},[a("span",[t._v("Обратная сторона формы № Т-55")])]),a("div",{staticClass:"row justify-center q-pa-sm"},[a("span",{staticClass:"uppercase"},[t._v("Табель использования рабочего времени")])]),a("div",{staticClass:"row"},[a("table",{staticClass:"fit tables",attrs:{border:"1",cellspacing:"0"}},[a("thead",[a("tr",[a("th",{attrs:{rowspan:"3"}},[t._v("Ф.И.О.")]),a("th",{attrs:{rowspan:"3",width:"10"}},[t._v("Профессия")]),a("th",{attrs:{rowspan:"3",width:"5"}},[t._v("Разряд")]),a("th",{attrs:{colspan:"16"}},[t._v("Отработано часов по числам месяца")]),a("th",{attrs:{colspan:"2"}},[t._v("Итого")]),a("th",{attrs:{rowspan:"3",width:"5"}},[t._v("Выпол"),a("br"),t._v("нено норм")]),a("th",{attrs:{colspan:"7"}},[t._v("Сумма начисления")])]),a("tr",[t._l(15,function(s){return a("th",[t._v(t._s(s))])}),a("th",[t._v(" ")]),a("th",{attrs:{rowspan:"2",width:"5"}},[t._v("Часов")]),a("th",{attrs:{rowspan:"2",width:"5"}},[t._v("Дней")]),a("th",{attrs:{rowspan:"2",width:"5"}},[t._v("тарифная"),a("br"),t._v("ставка")]),a("th",{attrs:{rowspan:"2",width:"5"}},[t._v("по"),a("br"),t._v("коэфф"),a("br"),t._v("ициенту")]),a("th",{attrs:{rowspan:"2",width:"5"}},[t._v("по условиям"),a("br"),t._v(" труда")]),a("th",{attrs:{rowspan:"2",width:"5"}},[t._v("по сдел. расц.")]),a("th",{attrs:{rowspan:"2",width:"5"}},[t._v("праздн"),a("br"),t._v("ичным")]),a("th",{attrs:{rowspan:"2",width:"5"}},[t._v("премия")]),a("th",{attrs:{rowspan:"2",width:"5"}},[t._v("всего")])],2),a("tr",t._l(16,function(s){return a("th",[t._v("\n                  "+t._s(s+15)+"\n                ")])}))]),a("tbody",[t._l(t.outfit.tables,function(s){return a("tr",{key:s.id,staticStyle:{height:"30px"}},[a("td",[t._v(t._s(s.worker.full_name))]),a("td",[t._v(t._s(s.worker.position))]),a("td",[t._v(t._s(s.rank))]),t._l(16,function(i){return a("td",{staticStyle:{padding:"0","white-space":"pre-line"}},[a("div",{staticClass:"flex flex-center bor-bot",staticStyle:{height:"15px"}},[t._v(t._s(s.workdays[i]))]),a("div",{staticClass:"flex flex-center",staticStyle:{height:"15px"}},[t._v(t._s(s.workdays[i+15]))])])}),a("td",[t._v(t._s(s.hours))]),a("td",[t._v(t._s(parseFloat(s.days)))]),a("td",[t._v(t._s(s.done))]),a("td",[t._v(t._s(s.tariff_rate))]),a("td",[t._v(t._s(s.by_coefficient))]),a("td",[t._v(t._s(s.by_conditions))]),a("td"),a("td"),a("td",[t._v(t._s(s.bonus))]),a("td",[t._v(t._s(s.total))])],2)}),t._l(12-t.outfit.tables.length,function(s){return a("tr",{staticStyle:{height:"30px"}},t._l(29,function(s){return a("td",[t._v(" ")])}))})],2),a("tfoot",[a("tr",{staticClass:"text-bold"},[a("td",[t._v("Итого:")]),a("td",{attrs:{colspan:"18"}}),a("td",[t._v(t._s(parseFloat(t.outfit.hours_total)))]),a("td",[t._v(t._s(parseFloat(t.outfit.days_total)))]),a("td",[t._v(t._s(t.outfit.done_total))]),a("td",[t._v(t._s(t.outfit.amount))]),a("td",[t._v(t._s(t.outfit.amount_coefficient))]),a("td",[t._v(t._s(t.outfit.amount_conditions))]),a("td"),a("td"),a("td",[t._v(t._s(t.outfit.amount_bonus))]),a("td",[t._v(t._s(t.outfit.amount_total))])])])])]),a("br"),a("br"),a("div",{staticClass:"row",staticStyle:{outline:"1px solid"}},[a("div",{staticClass:"col-7 q-pa-sm",staticStyle:{outline:"1px solid"}},[a("p",[t._v("Количество дней, разряд и коэффициент рабочим объявлены.")]),a("p",{staticClass:"row"},[a("span",{staticClass:"col-auto"},[t._v("Ответственный за ведение табеля:")]),a("span",{staticClass:"col-auto q-px-sm text-center pos bor-bot relative-position q-mx-xs"},[t._v(t._s(t.outfit.responsible.position))]),a("span",{staticClass:"col-2 sign text-center bor-bot relative-position q-mx-xs"}),a("span",{staticClass:"col-3 text-center sign-trans relative-position bor-bot"},[t._v(t._s(t.outfit.responsible.full_name))])]),a("p",{staticClass:"row"},[a("span",{staticClass:"col-auto"},[t._v("Расчет составил:")]),a("span",{staticClass:"col-auto q-px-sm text-center pos bor-bot relative-position q-mx-xs"},[t._v(t._s(t.outfit.calculated.position))]),a("span",{staticClass:"col-2 sign text-center bor-bot relative-position q-mx-xs"}),a("span",{staticClass:"col-3 text-center sign-trans relative-position bor-bot"},[t._v(t._s(t.outfit.calculated.full_name))])]),a("p",{staticClass:"row"},[a("span",{staticClass:"col-auto"},[t._v("Принял на ответственное хранение:")]),a("span",{staticClass:"col-auto q-px-sm text-center dat bor-bot relative-position q-mx-xs"},[t._v("\n                  "+t._s(new Date(t.outfit.date).toLocaleDateString())+"\n                ")]),a("span",{staticClass:"col-auto q-px-sm text-center pos bor-bot relative-position q-mx-xs"},[t._v(t._s(t.outfit.deposited.position))]),a("span",{staticClass:"col-2 sign text-center bor-bot relative-position q-mx-xs"}),a("span",{staticClass:"col text-center sign-trans relative-position bor-bot"},[t._v(t._s(t.outfit.deposited.full_name))])])]),a("div",{staticClass:"col-5 q-pa-sm"},[a("p",[t._v("Подлежит оприходыванию следующая лесопродукция (пиломатериалы):")]),a("table",{staticClass:"tables full-width",attrs:{border:"1",cellspacing:"0"}},[a("thead",[a("tr",[a("th",[t._v("Наименование")]),a("th",[t._v("Ед. изм.")]),a("th",[t._v("Количество")])])]),a("tbody",[t._l(t.outfit.postings,function(s){return a("tr",[a("td",[t._v(t._s(s.material.name))]),a("td",[t._v(t._s(s.material.units_full))]),a("td",[t._v(t._s(parseFloat(s.quantity)))])])}),t._l(6-t.outfit.postings.length,function(s){return a("tr",[a("td",[t._v(" ")]),a("td",[t._v(" ")]),a("td",[t._v(" ")])])})],2)])])])])],1):t._e()],1)],1)},o=[];i._withStripped=!0;var n={name:"OutfitsList",props:{id:{required:!0}},data:function(){return{outfit:null,options:{units:[{label:"M³",value:"MC"},{label:"M²",value:"MS"},{label:"Шт",value:"P"},{label:"Га",value:"HE"},{label:"Л",value:"L"}]}}},methods:{getOutfit:function(){var t=this;this.$axios.get("/api/v1/outfit/"+this.id+"/").then(function(s){t.outfit=s.data}).catch(function(s){t.$q.notify({message:s.message})})},print:function(){window.print()}},mounted:function(){this.getOutfit()}},e=n,r=(a("IVl5"),a("KHd+")),_=Object(r["a"])(e,i,o,!1,null,null,null);s["default"]=_.exports}}]);