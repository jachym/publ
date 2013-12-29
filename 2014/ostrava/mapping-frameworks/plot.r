# points
renderers<-read.table('results/result-points-rendering.txt', header=T)
png('graphs/result-points-rendering.png', width=800, height=480)
p <- barplot(as.matrix(renderers), axes=T, beside=T, legend=T, main="Time used for rendering N point features", ylab="Rendering time [s]")
abline(h=10*seq(6), col="gray", lty="dotted")
abline(h=1*seq(10), col="gray", lty="dotted")
dev.off()

renderers<-read.table('results/result-points-panning.txt', header=T)
png('graphs/result-points-panning.png', width=800, height=480)
p <- barplot(as.matrix(renderers), axes=T, beside=T, legend=T, main="Time used for panning N point features", ylab="Panning time [s]")
abline(h=10*seq(6), col="gray", lty="dotted")
abline(h=1*seq(10), col="gray", lty="dotted")
dev.off()

# lines
renderers<-read.table('results/result-lines-rendering.txt', header=T)
png('graphs/result-lines-rendering.png', width=800, height=480)
p <- barplot(as.matrix(renderers), axes=T, beside=T, legend=T, main="Time used for rendering N line features", ylab="Rendering time [s]")
abline(h=10*seq(6), col="gray", lty="dotted")
abline(h=1*seq(10), col="gray", lty="dotted")
dev.off()

renderers<-read.table('results/result-lines-panning.txt', header=T)
png('graphs/result-lines-panning.png', width=800, height=480)
p <- barplot(as.matrix(renderers), axes=T, beside=T, legend=T, main="Time used for panning N line features", ylab="Panning time [s]")
abline(h=10*seq(6), col="gray", lty="dotted")
abline(h=1*seq(10), col="gray", lty="dotted")
dev.off()

# polygons
renderers<-read.table('results/result-polygon-rendering.txt', header=T)
png('graphs/result-polygon-rendering.png', width=800, height=480)
p <- barplot(as.matrix(renderers), axes=T, beside=T, legend=T, main="Time used for rendering N polygon features", ylab="Rendering time [s]")
abline(h=10*seq(6), col="gray", lty="dotted")
abline(h=1*seq(10), col="gray", lty="dotted")
dev.off()

renderers<-read.table('results/result-polygon-panning.txt', header=T)
png('graphs/result-polygon-panning.png', width=800, height=480)
p <- barplot(as.matrix(renderers), axes=T, beside=T, legend=T, main="Time used for panning N polygon features", ylab="Panning time [s]")
abline(h=10*seq(6), col="gray", lty="dotted")
abline(h=1*seq(10), col="gray", lty="dotted")
dev.off()
