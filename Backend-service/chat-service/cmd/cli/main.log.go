package cli

import (
	"os"

	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

// format logs
func getEncoderLog() zapcore.Encoder {
	encodeConfig := zap.NewProductionEncoderConfig()
	encodeConfig.EncodeTime = zapcore.ISO8601TimeEncoder
	encodeConfig.TimeKey = "time"
	// from info INFO
	encodeConfig.EncodeLevel = zapcore.CapitalLevelEncoder
	// caller file
	encodeConfig.EncodeCaller = zapcore.ShortCallerEncoder
	return zapcore.NewConsoleEncoder(encodeConfig)
}

// write file
func getWriteSync() zapcore.WriteSyncer {
	file, _ := os.OpenFile(".log/log.txt", os.O_CREATE|os.O_WRONLY|os.O_APPEND, os.ModePerm)
	syncFile := zapcore.AddSync(file)
	syncConsole := zapcore.AddSync(os.Stderr)
	return zapcore.NewMultiWriteSyncer(syncConsole, syncFile)
}

func main() {
	encoder := getEncoderLog()
	sync := getWriteSync()
	core := zapcore.NewCore(encoder, sync, zapcore.InfoLevel)
	logger := zap.New(core, zap.AddCaller())

	logger.Info("Info Log", zap.Int("line", 1))
	logger.Error("Error log", zap.Int("line", 2))
}
