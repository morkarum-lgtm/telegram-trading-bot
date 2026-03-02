//@version=5
indicator("Telegram Signal Bot ELITE FIXED", overlay=true)

ema50 = ta.ema(close, 50)
ema200 = ta.ema(close, 200)
rsi = ta.rsi(close, 14)
adx = ta.adx(14)

highestHigh = ta.highest(high, 5)
lowestLow = ta.lowest(low, 5)

bullTrend = ema50 > ema200
bearTrend = ema50 < ema200
strongTrend = adx > 25

breakUp = close > highestHigh[1]
breakDown = close < lowestLow[1]

// signal conditions
callRaw = bullTrend and strongTrend and breakUp and rsi > 60
putRaw = bearTrend and strongTrend and breakDown and rsi < 40

// prevent repeating signals
callSignal = callRaw and not callRaw[1]
putSignal = putRaw and not putRaw[1]

alertcondition(callSignal, title="CALL", message="CALL")
alertcondition(putSignal, title="PUT", message="PUT")

plotshape(callSignal, style=shape.labelup, location=location.belowbar, color=color.green, text="CALL")
plotshape(putSignal, style=shape.labeldown, location=location.abovebar, color=color.red, text="PUT")
