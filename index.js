'use strict'

require('dotenv').config();
const { Telegraf } = require('telegraf')

//console.log(process.env);
//token=process.env.TOKEN;

const bot = new Telegraf(process.env.TOKEN)
bot.start((ctx) => ctx.reply('Welcome'))
bot.help((ctx) => ctx.reply('Send me a sticker'))
bot.on('sticker', (ctx) => ctx.reply('👍'))
bot.hears('hi', (ctx) => ctx.reply('Hey there'))
bot.launch()