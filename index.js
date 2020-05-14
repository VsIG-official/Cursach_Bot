'use strict'

require('dotenv').config();
const { Telegraf } = require('telegraf')

bot.use(Telegraf.log())

const bot = new Telegraf(process.env.TOKEN)
bot.start((ctx) => ctx.reply('Hi, my beloved human. I`m here to help make Your own To-Do Lists! To make new List write:"/newList"'))
bot.command('newList', (ctx) => ctx.reply('Bot started.'));

bot.help((ctx) => ctx.reply('Send me a sticker'))
bot.on('sticker', (ctx) => ctx.reply('👍'))
bot.hears('hi', (ctx) => ctx.reply('Hey there'))
bot.launch()