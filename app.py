//@version=5
indicator("INSTITUTIONAL SCORE MODEL", overlay=true)

// === 15m Trend ===
ema50_15 = request.security(syminfo.tickerid, "15", ta.ema(close, 50))
ema200_15 = request.security(syminfo.tickerid, "15", ta.ema(close, 200))

bullTrend = ema50_15 > ema200_15
bearTrend = ema50_15 < ema200_15

// === 5m Indicators ===
rsi = ta.rsi(close, 14)
adx = ta.adx(14)
atr = ta.atr(14)
atr_ma = ta.sma(atr, 14)
vol_ma = ta.sma(volume, 20)

highestHigh = ta.highest(high, 5)
lowestLow = ta.lowest(low, 5)

breakUp = close > highestHigh[1]
breakDown = close < lowestLow[1]

// === SCORE CALCULATION ===
callScore = 0.0
putScore = 0.0

// Trend
callScore += bullTrend ? 20 : 0
putScore += bearTrend ? 20 : 0

// Breakout
callScore += breakUp ? 20 : 0
putScore += breakDown ? 20 : 0

// ADX
callScore += adx > 25 ? 15 : 0
putScore += adx > 25 ? 15 : 0

// Volume
callScore += volume > vol_ma ? 15 : 0
putScore += volume > vol_ma ? 15 : 0

// ATR Expansion
callScore += atr > atr_ma ? 15 : 0
putScore += atr > atr_ma ? 15 : 0

// RSI Zone
callScore += (rsi > 50 and rsi < 65) ? 15 : 0
putScore += (rsi < 50 and rsi > 35) ? 15 : 0

// === FINAL SIGNAL (≥ 80)
callSignal = callScore >= 80 and not (callScore[1] >= 80)
putSignal = putScore >= 80 and not (putScore[1] >= 80)

// === Alerts
alertcondition(callSignal, title="CALL", message="CALL")
alertcondition(putSignal, title="PUT", message="PUT")

plotshape(callSignal, style=shape.labelup, location=location.belowbar, color=color.green, text="CALL")
plotshape(putSignal, style=shape.labeldown, location=location.abovebar, color=color.red, text="PUT")
