package response

const (
	ErrorCodeSuccess                       = 200 // Success
	ErrorCodeFailed                        = 500 // Failed
	ErrorCodeNotFound                      = 404 // Not Found
	ErrorCodeUnauthorized                  = 401 // Unauthorized
	ErrorCodeForbidden                     = 403 // Forbidden
	ErrorCodeMethodNotAllowed              = 405 // Method Not Allowed
	ErrorCodeNotAcceptable                 = 406 // Not Acceptable
	ErrorCodeNotImplemented                = 501 // Not Implemented
	ErrorCodeBadGateway                    = 502 // Bad Gateway
	ErrorCodeServiceUnavailable            = 503 // Service Unavailable
	ErrorCodeGatewayTimeout                = 504 // Gateway Timeout
	ErrorCodeHTTPVersionNotSupported       = 505 // HTTP Version Not Supported
	ErrorCodeVariantAlsoNegotiates         = 506 // Variant Also Negotiates
	ErrorCodeInsufficientStorage           = 507 // Insufficient Storage
	ErrorCodeLoopDetected                  = 508 // Loop Detected
	ErrorCodeNotExtended                   = 510 // Not Extended
	ErrorCodeNetworkAuthenticationRequired = 511 // Network Authentication Required
	ErrorCodeNetworkConnectTimeoutError    = 599 // Network Connect Timeout Error
	ErrorCodeNetworkReadTimeoutError       = 596 // Network Read Timeout Error
	ErrorCodeParamInvalid                  = 400 // Param Invalid
)

var msg = map[int]string{
	ErrorCodeSuccess:      "Success",
	ErrorCodeParamInvalid: "Email is invalid",
}
