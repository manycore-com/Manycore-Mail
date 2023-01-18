package io.manycore.receiver.http.platform

import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.manycore.receiver.http.config.Config
import io.manycore.receiver.http.app.httpReceiverModule
import io.manycore.receiver.http.koin.inject

actual fun startPlatformEngine() {
    val config by inject<Config>()
    embeddedServer(
        factory = Netty,
        port = config.appPort,
        host = config.appHost,
        module = Application::httpReceiverModule,
    ).start(true)
}
