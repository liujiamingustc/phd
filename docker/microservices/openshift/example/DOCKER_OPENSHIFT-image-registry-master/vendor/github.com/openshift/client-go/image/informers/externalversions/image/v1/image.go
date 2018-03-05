// This file was automatically generated by informer-gen

package v1

import (
	image_v1 "github.com/openshift/api/image/v1"
	versioned "github.com/openshift/client-go/image/clientset/versioned"
	internalinterfaces "github.com/openshift/client-go/image/informers/externalversions/internalinterfaces"
	v1 "github.com/openshift/client-go/image/listers/image/v1"
	meta_v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	runtime "k8s.io/apimachinery/pkg/runtime"
	watch "k8s.io/apimachinery/pkg/watch"
	cache "k8s.io/client-go/tools/cache"
	time "time"
)

// ImageInformer provides access to a shared informer and lister for
// Images.
type ImageInformer interface {
	Informer() cache.SharedIndexInformer
	Lister() v1.ImageLister
}

type imageInformer struct {
	factory          internalinterfaces.SharedInformerFactory
	tweakListOptions internalinterfaces.TweakListOptionsFunc
}

// NewImageInformer constructs a new informer for Image type.
// Always prefer using an informer factory to get a shared informer instead of getting an independent
// one. This reduces memory footprint and number of connections to the server.
func NewImageInformer(client versioned.Interface, resyncPeriod time.Duration, indexers cache.Indexers) cache.SharedIndexInformer {
	return NewFilteredImageInformer(client, resyncPeriod, indexers, nil)
}

// NewFilteredImageInformer constructs a new informer for Image type.
// Always prefer using an informer factory to get a shared informer instead of getting an independent
// one. This reduces memory footprint and number of connections to the server.
func NewFilteredImageInformer(client versioned.Interface, resyncPeriod time.Duration, indexers cache.Indexers, tweakListOptions internalinterfaces.TweakListOptionsFunc) cache.SharedIndexInformer {
	return cache.NewSharedIndexInformer(
		&cache.ListWatch{
			ListFunc: func(options meta_v1.ListOptions) (runtime.Object, error) {
				if tweakListOptions != nil {
					tweakListOptions(&options)
				}
				return client.ImageV1().Images().List(options)
			},
			WatchFunc: func(options meta_v1.ListOptions) (watch.Interface, error) {
				if tweakListOptions != nil {
					tweakListOptions(&options)
				}
				return client.ImageV1().Images().Watch(options)
			},
		},
		&image_v1.Image{},
		resyncPeriod,
		indexers,
	)
}

func (f *imageInformer) defaultInformer(client versioned.Interface, resyncPeriod time.Duration) cache.SharedIndexInformer {
	return NewFilteredImageInformer(client, resyncPeriod, cache.Indexers{cache.NamespaceIndex: cache.MetaNamespaceIndexFunc}, f.tweakListOptions)
}

func (f *imageInformer) Informer() cache.SharedIndexInformer {
	return f.factory.InformerFor(&image_v1.Image{}, f.defaultInformer)
}

func (f *imageInformer) Lister() v1.ImageLister {
	return v1.NewImageLister(f.Informer().GetIndexer())
}
